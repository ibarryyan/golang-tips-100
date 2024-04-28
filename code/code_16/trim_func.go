package code_16

import (
	"fmt"
	"strings"
)

func main() {
	str := "   Hello, World!   "
	// 去除字符串左侧的空格
	trimmed := strings.TrimLeft(str, " ")
	fmt.Println(trimmed) // 输出: "Hello, World!   "

	// 去除字符串左侧的多个特定字符
	strWithPrefix := "!!!Hello, World!!!"
	trimmedWithPrefix := strings.TrimLeft(strWithPrefix, "!")
	fmt.Println(trimmedWithPrefix) // 输出: "Hello, World!!!"

	// 去除字符串左侧的字符集合中的任意字符
	strWithChars := "abcHello, World!abc"
	trimmedWithChars := strings.TrimLeft(strWithChars, "abc")
	fmt.Println(trimmedWithChars) // 输出: "Hello, World!abc"
}
