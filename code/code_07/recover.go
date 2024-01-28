package code_07

import (
	"fmt"
	"testing"
)

func TestPanic(t *testing.T) {
	defer func() {
		if err := recover(); err != nil {
			fmt.Println(err)
			fmt.Println("发生panic后...")
		}
	}()
	fmt.Println("发生panic前...")
	panic("panic 啦 ~~~")
}
