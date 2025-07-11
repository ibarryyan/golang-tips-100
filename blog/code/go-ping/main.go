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

	fmt.Printf("\n--- %s (%s) ping statistics ---\n", s.Target, s.IP)
	fmt.Printf("%d packets transmitted, %d received, %.2f%% packet loss\n",
		s.Sent, s.Received, loss)
	if s.Received > 0 {
		fmt.Printf("rtt min/avg/max = %v/%v/%v\n", s.MinRTT, avg, s.MaxRTT)
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
	if err := p.ipv4Conn.SetTTL(p.TTL); err != nil {
		conn.Close()
		return nil, fmt.Errorf("无法设置TTL: %w", err)
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
	if err := p.ipv6Conn.SetHopLimit(p.TTL); err != nil {
		conn.Close()
		return nil, fmt.Errorf("无法设置Hop Limit: %w", err)
	}

	p.addr = &net.IPAddr{IP: ipAddr.IP}
	return p, nil
}

// Run 开始ping操作
func (p *Pinger) Run() {
	defer p.conn.Close()

	// 设置信号处理
	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt)
	go func() {
		<-c
		p.Stop()
	}()

	fmt.Printf("PING %s (%s):\n", p.stats.Target, p.stats.IP)

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
	p.wg.Wait()
	p.stats.print()
}

// Stop 停止ping操作
func (p *Pinger) Stop() {
	p.stopOnce.Do(func() {
		close(p.done)
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

			// 发送请求
			start := time.Now()
			if _, err := p.conn.WriteTo(wb, p.addr); err != nil {
				p.receiveChan <- &PingResult{
					Seq:   seq,
					Error: fmt.Errorf("发送ICMP消息失败: %w", err),
				}
				continue
			}

			// 更新统计
			p.stats.mu.Lock()
			p.stats.Sent++
			p.stats.mu.Unlock()

			// 设置接收超时
			deadline := start.Add(p.Timeout)
			if err := p.conn.SetReadDeadline(deadline); err != nil {
				p.receiveChan <- &PingResult{
					Seq:   seq,
					Error: fmt.Errorf("设置读取超时失败: %w", err),
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

			n, _, err := p.conn.ReadFrom(rb)
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

			// 提取TTL
			var ttl int
			if p.IPv6 {
				// 对于IPv6，我们无法直接从包中获取hop limit
				ttl = p.TTL
			} else {
				// 尝试从IPv4头获取TTL
				ttl = p.TTL // 默认值
				if p.ipv4Conn != nil {
					// 这里可以尝试获取实际TTL，但需要更复杂的处理
				}
			}

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

				// 创建结果
				p.receiveChan <- &PingResult{
					Seq:      echoReply.Seq,
					Size:     len(echoReply.Data),
					TTL:      ttl,
					RTT:      receiveTime.Sub(receiveTime.Add(-p.Timeout)),
					Received: true,
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
				fmt.Printf("%d bytes from %s: icmp_seq=%d ttl=%d time=%v\n",
					result.Size, p.stats.IP, result.Seq, result.TTL, result.RTT)
			}
		}
	}
}
