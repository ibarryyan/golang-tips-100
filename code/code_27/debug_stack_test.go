package code_27

import (
	"fmt"
	"runtime/debug"
)

func main() {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered from panic:", r)
			fmt.Println("Stack trace:")
			debug.PrintStack() // 或者使用 debug.Stack() 并将结果输出
		}
	}()

	// 触发一个panic作为示例
	panic("something went wrong")

	// 这行代码将不会被执行
	fmt.Println("This will not be printed")
}
