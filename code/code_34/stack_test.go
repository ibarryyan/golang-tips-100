package code_34

import "fmt"

//func f() {
//    l := []int{1, 2, 3, 4, 5}
//    for _, i := range l {
//        go fmt.Println(i)
//    }
//}

func f() {
	l := []int{1, 2, 3, 4, 5}
	for _, i := range l {
		go func(i int) {
			fmt.Println(i)
		}(i)
	}
}
