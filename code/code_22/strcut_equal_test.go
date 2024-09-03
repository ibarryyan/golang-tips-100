package code_22

import "fmt"

type Point struct {
	X, Y int
}

func main() {
	p1 := Point{1, 2}
	p2 := Point{1, 2}
	p3 := Point{2, 2}

	fmt.Println(p1 == p2) // 输出: true
	fmt.Println(p1 == p3) // 输出: false
}

type MyStruct struct {
	Value int
	Slice []int
}

func main2() {
	ms1 := MyStruct{Value: 1, Slice: []int{1, 2}}
	ms2 := MyStruct{Value: 1, Slice: []int{1, 2}}

	// 下面的比较会导致编译错误
	fmt.Println(ms1 == ms2) // 编译错误: invalid operation: ms1 == ms2 (struct containing []int cannot be compared)
}
