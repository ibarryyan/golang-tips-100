package code_42

import (
	"fmt"
	"testing"
	"time"
)

func TestAfter(t *testing.T) {
	for {
		select {
		case <-time.After(time.Second * 10):
			fmt.Println("timeout")
		}
	}
}

func TestTimer(t *testing.T) {
	for {
		timer := time.NewTimer(time.Second * 10)
		select {
		case <-timer.C:
			fmt.Println("timeout")
		}
		timer.Stop() // 手动释放
	}
}
