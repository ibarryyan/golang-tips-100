package code_25

import (
	"fmt"
	"sync"
	"sync/atomic"
)

var counter int64

func increment(wg *sync.WaitGroup) {
	defer wg.Done()
	for i := 0; i < 1000; i++ {
		atomic.AddInt64(&counter, 1)
	}
}

func main() {
	var wg sync.WaitGroup
	for i := 0; i < 100; i++ {
		wg.Add(1)
		go increment(&wg)
	}
	wg.Wait()
	fmt.Println("Final Counter:", counter) // 应为100 * 1000 = 100000
}
