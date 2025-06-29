package code_38

import (
	"fmt"
	"testing"
)

func TestNewAndMake(t *testing.T) {
	p := new(int)   // p 是 *int 类型，指向值为 0 的内存
	fmt.Println(*p) // 输出 0

	s := make([]int, 5)       // 创建长度为 5 的切片，底层数组已分配
	m := make(map[string]int) // 创建空 map（已初始化哈希表）
	ch := make(chan int, 10)  // 创建带缓冲的 channel

	fmt.Println(s) // 输出: [0 0 0 0 0]
	fmt.Println(m)
	fmt.Println(ch)
}
