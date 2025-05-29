package code_34

import (
	"fmt"
	"sync"
	"testing"
)

type Counter struct {
	sync.Mutex
	Count int
}

func foo(c Counter) {
	c.Lock()
	defer c.Unlock()
	fmt.Println("in foo")
}

func TestLock(t *testing.T) {
	var c Counter
	c.Lock()
	defer c.Unlock()
	c.Count++
	foo(c) // 复制锁
}
