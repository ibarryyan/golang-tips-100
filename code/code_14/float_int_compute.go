package main

import (
	"fmt"
)

func main() {
	// 定义两个float64类型的小数
	a := 3.14
	b := 2.71

	// 乘法
	product := a * b
	fmt.Printf("Product: %f\n", product)

	// 除法
	quotient := a / b
	fmt.Printf("Quotient: %f\n", quotient)
}

func main() {
	// 定义两个int32类型的变量
	a := int32(10)
	b := int32(3)

	// 将它们转换为float64类型以执行除法运算
	result := float64(a) / float64(b)

	// 使用fmt.Printf格式化输出，保留两位小数
	fmt.Printf("Result: %.2f\n", result)
}

func main() {
	// 定义两个int32类型的变量
	a := int32(10)
	b := int32(3)

	// 将它们转换为float64类型以执行除法运算
	result := float64(a) / float64(b)

	// 使用fmt.Printf格式化输出，保留两位小数
	fmt.Printf("Result: %.2f\n", result)
}
