package code_35

import (
	"log"
	"time"
)

func Run() {
	defer func() {
		if r := recover(); r != nil {
			log.Printf("ping panic: %v", r) // 这个recover只能捕获当前goroutine的panic
		}
	}()

	go func() {
		panic("panic")
	}()

	time.Sleep(time.Second * 3)
}
