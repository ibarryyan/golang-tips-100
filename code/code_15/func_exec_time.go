package code_15

import (
	"fmt"
	"testing"
	"time"
)

// 封装函数
func ExecTime(t time.Time) time.Duration {
	ts := time.Since(t)
	fmt.Println("ts:", ts)
	return ts
}

func main(t *testing.T) {
	defer ExecTime(time.Now()) //记录耗时

	time.Sleep(500 * time.Millisecond)
}
