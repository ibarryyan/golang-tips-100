package main

import (
	"fmt"
	"unsafe"
)

func Test(list []string) {
	fmt.Println(list)
	fmt.Println(unsafe.Pointer(&list))
}

func main() {
	list := make([]string, 0)
	list = append(list, "a", "b", "c")
	fmt.Println(list)
	fmt.Println(unsafe.Pointer(&list))
	Test(list)
}
