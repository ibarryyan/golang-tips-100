package code_21

import (
	"fmt"
	"testing"
	"time"
)

func TestHasBufferChannel(t *testing.T) {
	ch := make(chan int, 2) // 创建一个容量为2的带缓冲channel

	ch <- 10
	ch <- 20

	go func() {
		time.Sleep(time.Second * 2)
		ch <- 30 // 这条语句会阻塞，直到缓冲区有空间
	}()

	data := <-ch
	fmt.Println("Received data:", data)
	data = <-ch
	fmt.Println("Received data:", data)

	time.Sleep(time.Second * 3) // 等待足够的时间来接收最后一条数据
	data = <-ch
	fmt.Println("Received data:", data)
}