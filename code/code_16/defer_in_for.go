package code_16

import "fmt"

func main() {
	for i := 0; i < 5; i++ {
		defer fmt.Println(i)
	}

	for i := 0; i < 5; i++ {
		defer func(x int) {
			fmt.Println(x)
		}(i)
	}

}
