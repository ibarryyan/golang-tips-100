package main

import (
	"fmt"
)

func PlayFunc(str string, fn func() error) error {
	fmt.Println(str)

	defer func() {
		fmt.Println("defer 1 ...")
	}()

	defer func() {
		fmt.Println("defer 2 ...")
	}()

	return fn()
}

func main() {
	err := PlayFunc("string ...", func() error {
		fmt.Println("func ...")
		return nil
	})
	fmt.Println(err)
}
