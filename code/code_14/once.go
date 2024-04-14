package main

import (
	"fmt"
	"sync"
)

func main() {
	var once sync.Once

	// 定义一个初始化函数
	initFunc := func() {
		fmt.Println("Initialization function is called only once.")
	}

	// 模拟多个协程尝试调用初始化函数
	for i := 0; i < 5; i++ {
		go once.Do(initFunc)
	}

	// 等待所有协程执行完毕
	var wg sync.WaitGroup
	wg.Add(5)
	for i := 0; i < 5; i++ {
		go func() {
			defer wg.Done()
			once.Do(initFunc)
		}()
	}
	wg.Wait()
}
