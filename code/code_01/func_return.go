package main

import "fmt"

func Hello(name string) (str string) {
	str = "Hello World"
	if name != "" {
		return "Hello " + name
	}
	return
}

func Func1() (string, string) {
	return "A", "B"
}

func Func2() string {
	return "A"
}

func main() {
	fmt.Println(Hello(""))
	fmt.Println(Hello("zs"))

	_, _ = Func1()
	_ = Func2()
}
