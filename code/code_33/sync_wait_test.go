package code_33

import "sync"

var (
	wg sync.WaitGroup
)

func err() {
	// 危险用法
	for i := 0; i < 10; i++ {
		go func() {
			wg.Add(1) // 并发写入导致竞态
			defer wg.Done()
		}()
	}
}

func ok() {
	// 安全用法
	for i := 0; i < 10; i++ {
		wg.Add(1) // 在goroutine外部提前Add
		go func() {
			defer wg.Done()
		}()
	}
	wg.Wait()
}
