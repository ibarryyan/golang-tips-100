package code_26

import (
	"fmt"
	"testing"
	"unsafe"
)

func TestStringToByteArray(t *testing.T) {
	// 定义一个字符串
	str := "Hello, World!"

	// 将字符串转换为字节数组
	byteArray := []byte(str)

	// 打印字符串和字节数组的内容
	fmt.Println("String:", str)
	fmt.Println("Byte Array:", byteArray)

	// 打印字符串和字节数组的内存地址
	fmt.Printf("Address of string data: %p\n", unsafe.Pointer(&str))
	fmt.Printf("Address of byte array: %p\n", unsafe.Pointer(&byteArray))

	// 修改字节数组中的元素，验证它是独立的副本
	byteArray[0] = 'h'
	fmt.Println("Modified Byte Array:", byteArray)
	fmt.Println("String after modification (should be unchanged):", str)
}
