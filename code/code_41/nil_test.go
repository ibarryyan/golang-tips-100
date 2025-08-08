package code_41

import "testing"

func TestNil(t *testing.T) {
	var i int     // 0
	var f float64 // 0.0
	var b bool    // false
	var s string  // ""

	t.Log(i, f, b, s)
}

func TestNil2(t *testing.T) {
	var p *int           // nil 指针
	var sl []int         // nil 切片
	var m map[string]int // nil 映射
	var ch chan int      // nil 通道
	var f func()         // nil 函数
	var i interface{}    // nil 接口

	t.Log(p, sl, m, ch, f, i)
}

type Person struct {
	Name string
	Age  int
}
