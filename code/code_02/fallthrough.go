package code_02

import "fmt"

func main() {
	i := 10
	switch i {
	case 1:
		fmt.Println(1)
	case 5:
		fmt.Println(5)
		fallthrough
	case 10:
		fmt.Println(10)
		fallthrough
	case 20:
		fmt.Println(20)
	default:
		fmt.Println("default")
	}
}
