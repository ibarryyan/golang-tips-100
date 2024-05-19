package main

/*
#include "hello.c"
*/
import "C"
import "fmt"

func main() {
	fmt.Println("Calling C function...")
	C.sayHello() // 调用 C 函数
}
