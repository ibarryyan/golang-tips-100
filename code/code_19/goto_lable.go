package main

import "fmt"

func main() {
	i := 0

Here: // Label
	fmt.Println(i)
	i++
	if i < 5 {
		goto Here // 跳转到标签Here
	}
	fmt.Println("Done")

	// call f1()
	fmt.Println("f1...")
	f1()

	fmt.Println("f2...")
	f2()
}

func f1() {
BreakPoint2:
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if i*j > 4 {
				break BreakPoint2
			}
			fmt.Println(i, "*", j, "=", i*j)
		}
		fmt.Println(i, "*", i)
	}
}

func f2() {
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if i*j > 4 {
				goto BreakPoint
			}
			fmt.Println(i, "*", j, "=", i*j)
		}
		fmt.Println(i, "*", i)
	}
BreakPoint:
	fmt.Println("跳出循环")
}
