package code_39

import (
	"fmt"
	"sync"
	"sync/atomic"
)

func main1() {
	s := make([]int, 0)
	var wg sync.WaitGroup

	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func() {
			s = append(s, 1) // 并发追加
			wg.Done()
		}()
	}

	wg.Wait()
	fmt.Println(len(s)) // 结果可能 <1000（数据丢失）
}

func main2() {
	s := make([]int, 0, 10)
	var wg sync.WaitGroup

	for i := 0; i < 100; i++ {
		wg.Add(1)
		go func(i int) {
			if len(s) < cap(s) {
				s = append(s, i) // 可能同时触发扩容
			}
			wg.Done()
		}(i)
	}

	wg.Wait()
	fmt.Println(s) // 可能包含重复值或乱码
}

// 方案 1：互斥锁保护（推荐）

type SafeSlice struct {
	sync.RWMutex
	items []int
}

func (ss *SafeSlice) Append(item int) {
	ss.Lock()
	defer ss.Unlock()
	ss.items = append(ss.items, item)
}

func (ss *SafeSlice) Get(index int) (int, bool) {
	ss.RLock()
	defer ss.RUnlock()
	if index >= len(ss.items) {
		return 0, false
	}
	return ss.items[index], true
}

// 方案 2：通道串行化访问

func sliceManager(ch chan int) []int {
	s := make([]int, 0)
	for item := range ch { // 通过通道顺序处理
		s = append(s, item)
	}
	return s
}

func main3() {
	ch := make(chan int)
	go func() {
		ch <- 1 // 通过通道安全添加
		ch <- 2
		close(ch)
	}()
	result := sliceManager(ch)
	fmt.Println(result) // 输出: [1 2]
}

// 方案 3：预分配 + 独立索引

func main4() {
	s := make([]int, 1000) // 预分配
	var wg sync.WaitGroup
	var counter int32

	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func() {
			idx := atomic.AddInt32(&counter, 1) - 1
			s[idx] = 1 // 每个goroutine写独立位置
			wg.Done()
		}()
	}
	wg.Wait()
}
