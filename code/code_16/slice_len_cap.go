package code_16

import "fmt"

func SliceLenAndCap1() {
	list := make([]int, 0)
	fmt.Printf("list elements = %+v , len = %d , cap = %d \n", list, len(list), cap(list))
	newList := append(list, 1, 2, 3)
	fmt.Printf("list elements = %+v , len = %d , cap = %d \n", newList, len(newList), cap(newList))
	newList2 := append(newList, 4)
	fmt.Printf("list elements = %+v , len = %d , cap = %d \n", newList2, len(newList2), cap(newList2))

	// 输出：
	//list elements = [] , len = 0 , cap = 0
	//list elements = [1 2 3] , len = 3 , cap = 3
	//list elements = [1 2 3 4] , len = 4 , cap = 6
}

func SliceLenAndCap2() {
	list := []int{1, 2, 3}
	fmt.Printf("list elements = %+v , len = %d , cap = %d \n", list, len(list), cap(list))
	newList := append(list, 4)
	fmt.Printf("list elements = %+v , len = %d , cap = %d \n", newList, len(newList), cap(newList))

	// 输出：
	//list elements = [1 2 3] , len = 3 , cap = 3
	//list elements = [1 2 3 4] , len = 4 , cap = 6
}
