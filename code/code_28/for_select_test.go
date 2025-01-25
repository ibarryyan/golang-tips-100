package code_28

import (
	"fmt"
	"testing"
	"time"
)

func TestForSelect(t *testing.T) {
	ch1 := make(chan int)
	ch2 := make(chan string)

	go func() {
		for i := 0; i < 5; i++ {
			ch1 <- i
			time.Sleep(time.Second)
		}
		close(ch1)
	}()

	go func() {
		for i := 0; i < 5; i++ {
			ch2 <- fmt.Sprintf("message %d", i)
			time.Sleep(2 * time.Second)
		}
		close(ch2)
	}()

	for {
		select {
		case num, ok := <-ch1:
			if !ok {
				ch1 = nil // 通道关闭后设置为 nil，避免重复关闭
			} else {
				fmt.Println("Received from ch1:", num)
			}
		case msg, ok := <-ch2:
			if !ok {
				ch2 = nil // 通道关闭后设置为 nil，避免重复关闭
			} else {
				fmt.Println("Received from ch2:", msg)
			}
		case <-time.After(3 * time.Second):
			fmt.Println("Timeout")
		default:
			fmt.Println("No data received")
			time.Sleep(time.Second)
		}

		// 当所有通道都关闭时退出循环
		if ch1 == nil && ch2 == nil {
			break
		}
	}
}
