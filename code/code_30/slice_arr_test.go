package code_30

import (
	"fmt"
	"testing"
)

func TestSlice(t *testing.T) {
	// 定义原始切片
	original := []int{1, 2, 3, 4, 5} // -> original: [1 2 3 4 5]

	slice1 := original[1:4] // -> slice1: [2 3 4]
	slice2 := original[2:]  // -> slice2: [3 4 5]

	// 修改slice1的第一个元素（会影响底层数组和其他切片）
	slice1[0] = 100

	// 打印结果
	fmt.Println(original) // [1 100 3 4 5]
	fmt.Println(slice2)   // [3 4 5]
}
