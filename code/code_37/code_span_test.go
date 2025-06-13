package code_37

import "fmt"

func main() {
	x := 1
	{
		x := 2
		fmt.Print(x)
	}
	fmt.Println(x)
}
