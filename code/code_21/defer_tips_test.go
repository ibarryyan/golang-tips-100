package code_21

import (
	"fmt"
	"testing"
)

var str string

func hello() func() {
	str = "Hello World"
	fmt.Println("This is hello() func ...")
	return func() {
		fmt.Println("This is return func() ...")
	}
}

func TestDeferReturnFunc(t *testing.T) {
	defer hello()
	fmt.Println("This is test func , str = ",str)
}

func TestDeferReturnFuncCall(t *testing.T) {
	defer hello()()
	fmt.Println("This is test func , str = ",str)
}