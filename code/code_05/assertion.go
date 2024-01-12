package code_05

import "fmt"

func main() {
	var value interface{}
	value = "hello"
	str := value.(string)
	fmt.Println(str)

	value = 100
	i := value.(int32)
	fmt.Println(i)
}

func main2() {
	var value interface{}
	value = 100
	switch value.(type) {
	case int32:
		fmt.Println(value.(int32))
	case string:
		fmt.Println(value.(string))
	case int:
		fmt.Println(value.(int))
	}
}
