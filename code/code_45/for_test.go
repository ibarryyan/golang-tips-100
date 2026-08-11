package code_45

import (
	"fmt"
	"sync"
	"testing"
	"time"
)

func TestFor(t *testing.T) {
	var wg sync.WaitGroup
	values := []int{1, 2, 3}

	for _, v := range values {
		wg.Add(1)
		go func() {
			defer wg.Done()
			time.Sleep(time.Second * 10)
			fmt.Println(v) // ⚠️ 总是打印 3
		}()
	}

	wg.Wait()
}
