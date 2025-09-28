package code_43

import (
	"context"
	"fmt"
	"time"
)

func worker() {
	for {
		fmt.Println("working...")
		time.Sleep(time.Second)
	}
}

func main() {
	go worker()
	time.Sleep(3 * time.Second)
	fmt.Println("main exit")
}

func worker1(stop chan struct{}) {
	for {
		select {
		case <-stop:
			fmt.Println("worker stopped")
			return
		default:
			fmt.Println("working...")
			time.Sleep(time.Second)
		}
	}
}

func main1() {
	stop := make(chan struct{})
	go worker1(stop)
	time.Sleep(3 * time.Second)
	close(stop) // 发送退出信号
}

func worker2(ctx context.Context) {
	for {
		select {
		case <-ctx.Done():
			fmt.Println("worker stopped")
			return
		default:
			fmt.Println("working...")
			time.Sleep(time.Second)
		}
	}
}

func main2() {
	ctx, cancel := context.WithCancel(context.Background())
	go worker2(ctx)
	time.Sleep(3 * time.Second)
	cancel() // 结束 goroutine
}
