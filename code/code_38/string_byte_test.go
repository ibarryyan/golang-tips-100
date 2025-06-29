package code_38

import (
	"fmt"
	"testing"
)

func TestStrAndByte(t *testing.T) {
	main()
}

func main() {
	// string → []byte
	s := "Hello, 世界"
	b := []byte(s)
	b[7] = 0xE4            // 修改 "世" 的 UTF-8 字节（需谨慎处理编码）
	fmt.Println(string(b)) // 输出可能乱码（需正确处理 Unicode）

	// 处理 Unicode 字符
	r := []rune(s)         // 将字符串转为 Unicode 码点切片
	r[7] = '新'             // 修改字符
	fmt.Println(string(r)) // 输出 "Hello, 新界"
}
