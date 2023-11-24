package main

import (
	"fmt"
	"sync"
)

func main() {
	waitGroup := sync.WaitGroup{}
	waitGroup.Add(1)
	go func() {
		defer func() {
			if e := recover(); e != nil {
				fmt.Println("recover panic")
			}
			waitGroup.Done()
		}()
		fmt.Println("Hello goroutine ...")
		panic("err")
	}()
	waitGroup.Wait()
	fmt.Println("Hello main ...")
}