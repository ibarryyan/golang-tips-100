package main

import (
	"flag"
	"fmt"
	"log"
	"net"
	"os"
	"os/signal"
	"sync"
	"time"

	"golang.org/x/net/icmp"
	"golang.org/x/net/ipv4"
	"golang.org/x/net/ipv6"
)

const (
	protocolICMP     = 1  // IPv4 ICMP协议号
	protocolIPv6ICMP = 58 // IPv6 ICMP协议号
)

// PingResult 表示单个ping请求的结果
type PingResult struct {
	Seq      int
	Size     int
	TTL      int
	RTT      time.Duration
	Error    error
	Received bool
	SendTime time.Time // 添加发送时间字段
}

// PingStats 表示ping统计信息
type PingStats struct {
	Target   string
	IP       string
	Sent     int
	Received int
	MinRTT   time.Duration
	MaxRTT   time.Duration
	TotalRTT time.Duration
	mu       sync.Mutex // 保护并发访问
}

// 更新统计信息
func (s *PingStats) update(result PingResult) {
	s.mu.Lock()
	defer s.mu.Unlock()

	if result.Received {
		s.Received++
		s.TotalRTT += result.RTT

		if s.MinRTT == 0 || result.RTT < s.MinRTT {
			s.MinRTT = result.RTT
		}
		if result.RTT > s.MaxRTT {
			s.MaxRTT = result.RTT
		}
	}
}

// 打印统计信息
func (s *PingStats) print() {
	s.mu.Lock()
	defer s.mu.Unlock()

	loss := float64(0)
	if s.Sent > 0 {
		loss = float64(s.Sent-s.Received) / float64(s.Sent) * 100
	}

	avg := time.Duration(0)
	if s.Received > 0 {
		avg = s.TotalRTT / time.Duration(s.Received)
	}

	// 转换为毫秒并保留两位小数
	minMs := float64(s.MinRTT.Microseconds()) / 1000.0
	avgMs := float64(avg.Microseconds()) / 1000.0
	maxMs := float64(s.MaxRTT.Microseconds()) / 1000.0

	fmt.Printf("\n--- %s (%s) ping statistics ---\n", s.Target, s.IP)
	fmt.Printf("%d packets transmitted, %d received, %.2f%% packet loss\n",
		s.Sent, s.Received, loss)
	if s.Received > 0 {
		fmt.Printf("rtt min/avg/max = %.2f/%.2f/%.2f ms\n", minMs, avgMs, maxMs)
	}
}

// Pinger 表示ping工具
type Pinger struct {
	Target      string        // 目标主机名或IP
	Count       int           // ping次数，0表示无限
	Interval    time.Duration // ping间隔
	Timeout     time.Duration // 单个ping超时
	Size        int           // 数据包大小
	TTL         int           // 生存时间
	ID          int           // ICMP标识符
	IPv6        bool          // 是否使用IPv6
	stats       PingStats     // 统计信息
	conn        net.PacketConn
	ipv4Conn    *ipv4.PacketConn
	ipv6Conn    *ipv6.PacketConn
	addr        net.Addr
	sequence    int
	done        chan bool
	wg          sync.WaitGroup
	stopOnce    sync.Once
	sendChan    chan *icmp.Message
	receiveChan chan *PingResult
}

// NewPinger 创建一个新的Pinger实例
func NewPinger(target string) (*Pinger, error) {
	p := &Pinger{
		Target:      target,
		Count:       4,
		Interval:    time.Second,
		Timeout:     time.Second * 2,
		Size:        56,
		TTL:         64,
		ID:          os.Getpid() & 0xffff,
		done:        make(chan bool),
		sendChan:    make(chan *icmp.Message),
		receiveChan: make(chan *PingResult, 5),
	}

	// 解析目标地址
	ipAddr, err := net.ResolveIPAddr("ip", target)
	if err != nil {
		return nil, fmt.Errorf("无法解析目标地址: %w", err)
	}

	p.stats.Target = target
	p.stats.IP = ipAddr.String()
	p.IPv6 = ipAddr.IP.To4() == nil

	// 创建适当的连接
	if p.IPv6 {
		return p.setupIPv6(ipAddr)
	}
	return p.setupIPv4(ipAddr)
}

// 设置IPv4连接
func (p *Pinger) setupIPv4(ipAddr *net.IPAddr) (*Pinger, error) {
	conn, err := net.ListenPacket("ip4:icmp", "0.0.0.0")
	if err != nil {
		return nil, fmt.Errorf("无法创建IPv4 ICMP连接: %w", err)
	}

	p.conn = conn
	p.ipv4Conn = ipv4.NewPacketConn(conn)

	// 设置TTL
	if err := p.ipv4Conn.SetTTL(p.TTL); err != nil {
		conn.Close()
		return nil, fmt.Errorf("无法设置TTL: %w", err)
	}

	// 设置控制消息标志，以便我们可以读取TTL
	if err := p.ipv4Conn.SetControlMessage(ipv4.FlagTTL, true); err != nil {
		log.Printf("警告: 无法设置IPv4控制消息标志: %v", err)
	}

	p.addr = &net.IPAddr{IP: ipAddr.IP}
	return p, nil
}

// 设置IPv6连接
func (p *Pinger) setupIPv6(ipAddr *net.IPAddr) (*Pinger, error) {
	conn, err := net.ListenPacket("ip6:ipv6-icmp", "::")
	if err != nil {
		return nil, fmt.Errorf("无法创建IPv6 ICMP连接: %w", err)
	}

	p.conn = conn
	p.ipv6Conn = ipv6.NewPacketConn(conn)

	// 设置Hop Limit
	if err := p.ipv6Conn.SetHopLimit(p.TTL); err != nil {
		conn.Close()
		return nil, fmt.Errorf("无法设置Hop Limit: %w", err)
	}

	// 设置控制消息标志，以便我们可以读取Hop Limit
	if err := p.ipv6Conn.SetControlMessage(ipv6.FlagHopLimit, true); err != nil {
		log.Printf("警告: 无法设置IPv6控制消息标志: %v", err)
	}

	p.addr = &net.IPAddr{IP: ipAddr.IP}
	return p, nil
}

// Run 开始ping操作
func (p *Pinger) Run() {
	defer p.conn.Close()

	// 设置信号处理，捕获更多类型的终止信号
	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt, os.Kill)
	go func() {
		sig := <-c
		fmt.Printf("\n收到信号 %v，正在停止...\n", sig)
		p.Stop()
	}()

	fmt.Printf("PING %s (%s) %d(%d) bytes of data:\n",
		p.stats.Target, p.stats.IP, p.Size, p.Size+8) // 8 bytes for ICMP header

	// 启动接收goroutine
	p.wg.Add(1)
	go p.receiver()

	// 启动发送goroutine
	p.wg.Add(1)
	go p.sender()

	// 启动结果处理goroutine
	p.wg.Add(1)
	go p.resultHandler()

	// 等待完成
	<-p.done
	close(p.receiveChan) // 关闭接收通道，确保resultHandler能够退出
	p.wg.Wait()
	p.stats.print()
}

// Stop 停止ping操作
func (p *Pinger) Stop() {
	p.stopOnce.Do(func() {
		close(p.done) // 通知所有goroutine退出

		// 设置一个短暂的超时，以便读取操作能够及时返回
		if p.conn != nil {
			p.conn.SetReadDeadline(time.Now().Add(100 * time.Millisecond))
		}
	})
}

func main() {
	// 解析命令行参数
	var (
		count    = flag.Int("c", 4, "发送的ping包数量 (0 = 无限)")
		interval = flag.Duration("i", time.Second, "发送间隔")
		timeout  = flag.Duration("W", time.Second*2, "等待响应超时时间")
		size     = flag.Int("s", 56, "发送的数据包大小")
		ttl      = flag.Int("t", 64, "生存时间")
	)
	flag.Parse()

	if flag.NArg() < 1 {
		fmt.Println("Usage: go-ping [-c count] [-i interval] [-W timeout] [-s size] [-t ttl] <host>")
		os.Exit(1)
	}

	target := flag.Arg(0)

	// 创建并配置Pinger
	pinger, err := NewPinger(target)
	if err != nil {
		log.Fatalf("创建Pinger失败: %v", err)
	}

	// 应用命令行参数
	pinger.Count = *count
	pinger.Interval = *interval
	pinger.Timeout = *timeout
	pinger.Size = *size
	pinger.TTL = *ttl

	// 运行ping
	pinger.Run()
}

// 发送ICMP包
func (p *Pinger) sender() {
	defer p.wg.Done()

	seq := 0
	ticker := time.NewTicker(p.Interval)
	defer ticker.Stop()

	for {
		select {
		case <-p.done:
			return
		case <-ticker.C:
			if p.Count > 0 && seq >= p.Count {
				p.Stop()
				return
			}

			seq++
			p.sequence = seq

			// 创建ICMP消息
			var typ icmp.Type
			if p.IPv6 {
				typ = ipv6.ICMPTypeEchoRequest
			} else {
				typ = ipv4.ICMPTypeEcho
			}

			// 创建数据负载
			payload := make([]byte, p.Size)
			for i := range payload {
				payload[i] = byte(i & 0xff)
			}

			msg := &icmp.Message{
				Type: typ,
				Code: 0,
				Body: &icmp.Echo{
					ID:   p.ID,
					Seq:  seq,
					Data: payload,
				},
			}

			// 序列化消息
			wb, err := msg.Marshal(nil)
			if err != nil {
				p.receiveChan <- &PingResult{
					Seq:   seq,
					Error: fmt.Errorf("序列化ICMP消息失败: %w", err),
				}
				continue
			}

			// 记录发送时间
			sendTime := time.Now()

			// 将消息发送到sendChan通道
			select {
			case p.sendChan <- msg:
			default:
				// 如果通道已满，不阻塞
			}

			// 发送请求
			if _, err := p.conn.WriteTo(wb, p.addr); err != nil {
				p.receiveChan <- &PingResult{
					Seq:      seq,
					Error:    fmt.Errorf("发送ICMP消息失败: %w", err),
					SendTime: sendTime,
				}
				continue
			}

			// 更新统计
			p.stats.mu.Lock()
			p.stats.Sent++
			p.stats.mu.Unlock()

			// 设置接收超时
			deadline := sendTime.Add(p.Timeout)
			if err := p.conn.SetReadDeadline(deadline); err != nil {
				p.receiveChan <- &PingResult{
					Seq:      seq,
					Error:    fmt.Errorf("设置读取超时失败: %w", err),
					SendTime: sendTime,
				}
			}
		}
	}
}

// 接收ICMP包
func (p *Pinger) receiver() {
	defer p.wg.Done()

	// 创建接收缓冲区
	rb := make([]byte, 1500)

	// 创建一个映射来存储发送时间
	sendTimeMap := make(map[int]time.Time)
	var mapMutex sync.Mutex

	// 监听发送的消息，记录发送时间
	// 将此goroutine添加到WaitGroup以确保程序退出时它也能正确退出
	p.wg.Add(1)
	go func() {
		defer p.wg.Done()
		for {
			select {
			case <-p.done:
				return
			case msg := <-p.sendChan:
				if echo, ok := msg.Body.(*icmp.Echo); ok {
					mapMutex.Lock()
					sendTimeMap[echo.Seq] = time.Now()
					mapMutex.Unlock()
				}
			}
		}
	}()

	for {
		select {
		case <-p.done:
			return
		default:
			// 接收响应
			if err := p.conn.SetReadDeadline(time.Now().Add(p.Timeout)); err != nil {
				log.Printf("设置读取超时失败: %v", err)
				continue
			}

			var n int
			var err error
			var ttl int = p.TTL // 默认使用设置的TTL值

			// 根据IPv4/IPv6使用不同的读取方法来获取控制消息
			if p.IPv6 {
				if p.ipv6Conn != nil {
					var cm *ipv6.ControlMessage
					n, cm, _, err = p.ipv6Conn.ReadFrom(rb)
					if err == nil && cm != nil {
						ttl = cm.HopLimit
					}
				} else {
					n, _, err = p.conn.ReadFrom(rb)
				}
			} else {
				if p.ipv4Conn != nil {
					var cm *ipv4.ControlMessage
					n, cm, _, err = p.ipv4Conn.ReadFrom(rb)
					if err == nil && cm != nil {
						ttl = cm.TTL
					}
				} else {
					n, _, err = p.conn.ReadFrom(rb)
				}
			}

			if err != nil {
				if netErr, ok := err.(net.Error); ok && netErr.Timeout() {
					// 超时，继续等待下一个包
					continue
				}
				log.Printf("读取响应失败: %v", err)
				continue
			}

			// 获取接收时间
			receiveTime := time.Now()

			// 解析响应
			var proto int
			if p.IPv6 {
				proto = protocolIPv6ICMP
			} else {
				proto = protocolICMP
			}

			rm, err := icmp.ParseMessage(proto, rb[:n])
			if err != nil {
				log.Printf("解析ICMP消息失败: %v", err)
				continue
			}

			// TTL已经在ReadFrom时获取

			// 处理响应
			switch rm.Type {
			case ipv4.ICMPTypeEchoReply, ipv6.ICMPTypeEchoReply:
				echoReply, ok := rm.Body.(*icmp.Echo)
				if !ok {
					continue
				}

				if echoReply.ID != p.ID {
					continue // 忽略不匹配的响应
				}

				// 获取发送时间并计算RTT
				mapMutex.Lock()
				sendTime, exists := sendTimeMap[echoReply.Seq]
				if !exists {
					sendTime = receiveTime.Add(-p.Timeout) // 如果找不到发送时间，使用估计值
				}
				delete(sendTimeMap, echoReply.Seq) // 清理已使用的条目
				mapMutex.Unlock()

				rtt := receiveTime.Sub(sendTime)

				// 创建结果
				p.receiveChan <- &PingResult{
					Seq:      echoReply.Seq,
					Size:     len(echoReply.Data),
					TTL:      ttl,
					RTT:      rtt,
					Received: true,
					SendTime: sendTime,
				}
			default:
				// 忽略其他类型的ICMP消息
			}
		}
	}
}

// 处理ping结果
func (p *Pinger) resultHandler() {
	defer p.wg.Done()

	for {
		select {
		case <-p.done:
			return
		case result := <-p.receiveChan:
			if result.Error != nil {
				log.Printf("Ping错误 (seq=%d): %v", result.Seq, result.Error)
				continue
			}

			if result.Received {
				p.stats.update(*result)
				// 格式化RTT为毫秒，保留两位小数
				rttMs := float64(result.RTT.Microseconds()) / 1000.0
				fmt.Printf("%d bytes from %s: icmp_seq=%d ttl=%d time=%.2f ms\n",
					result.Size, p.stats.IP, result.Seq, result.TTL, rttMs)
			}
		}
	}
}
