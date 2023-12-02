package code_04

import "fmt"

const (
	i1 = iota
	i2

	n1 = iota * 10
	n2
	n3
)

func main() {
	fmt.Println(i1)
	fmt.Println(i2)

	fmt.Println(n1)
	fmt.Println(n2)
	fmt.Println(n3)
}
