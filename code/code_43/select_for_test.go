package code_43

import (
	"fmt"
	"testing"
	"time"
)

func TestFail(t *testing.T) {
	ch := make(chan int)
	for {
		select {
		case v := <-ch:
			fmt.Println("receive:", v)
		}
	}
}

func TestWay1(t *testing.T) {
	ch := make(chan int)
	for {
		select {
		case v := <-ch:
			fmt.Println("receive:", v)
		default:
			// 没数据就先干点别的
			time.Sleep(10 * time.Millisecond)
		}
	}
}

func TestWay2(t *testing.T) {
	ch := make(chan int)
	go func(ch chan int) {
		for i := 0; i < 3; i++ {
			ch <- i
		}
		close(ch)
	}(ch)

	for v := range ch {
		fmt.Println("receive:", v)
	}
}
