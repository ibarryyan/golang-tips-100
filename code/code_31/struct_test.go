package code_31

import (
	"encoding/json"
	"fmt"
	"unsafe"
)

// 未对齐的结构体 (24 bytes)
type BadStruct struct {
	a bool  // 1 byte
	b int64 // 8 bytes
	c bool  // 1 byte
}

// 对齐优化后的结构体 (16 bytes)
type GoodStruct struct {
	b int64 // 8 bytes（偏移量 0）
	a bool  // 1 byte（偏移量 8）
	c bool  // 1 byte（偏移量 9）
	// 自动填充 6 bytes 到 16 bytes（满足 8 字节对齐）
}

func main() {
	fmt.Println(unsafe.Sizeof(BadStruct{}))  // 输出 24
	fmt.Println(unsafe.Sizeof(GoodStruct{})) // 输出 16
}

type Set map[string]struct{}

func (s Set) Add(key string) {
	s[key] = struct{}{}
}

func (s Set) Contains(key string) bool {
	_, ok := s[key]
	return ok
}

func way1() {
	// 使用示例
	s := make(Set)
	s.Add("apple")
	fmt.Println(s.Contains("apple")) // true
}

func worker(stopCh <-chan struct{}) {
	for {
		select {
		case <-stopCh:
			return
		default:
			// 执行任务
		}
	}
}

func way2() {
	// 发送关闭信号
	closeCh := make(chan struct{})
	go worker(closeCh)
	close(closeCh) // 广播关闭
}

type Logger struct{}

func (Logger) Info(msg string) {
	fmt.Printf("[INFO] %s\n", msg)
}

func way3() {
	// 使用零内存接收器
	var log Logger
	log.Info("service started")
}

func way4() {
	// 限制并发数为 10
	sem := make(chan struct{}, 10)
	for i := 0; i < 1000; i++ {
		sem <- struct{}{}
		go func() {
			defer func() { <-sem }()
			// 业务逻辑
		}()
	}
}

type Marker interface {
	isMarker()
}

type MyMarker struct{}

func (MyMarker) isMarker() {}

// 类型断言检查
func CheckMarker(v interface{}) bool {
	_, ok := v.(Marker)
	return ok
}

type Response struct {
	Data  interface{} `json:"data"`
	Error struct{}    `json:"error,omitempty"`
}

func way6() {
	// 序列化时自动忽略空 error 字段
	resp := Response{Data: "success"}
	jsonData, _ := json.Marshal(resp) // {"data":"success"}
	fmt.Println(string(jsonData))
}
