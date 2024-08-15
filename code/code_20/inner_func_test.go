package code_20

import (
    "testing"
    "fmt"
)

func userInnerFunc(t *testing.T) {
	// append
	var nums []int
	for i := 0; i < 10; i++ {
		nums = append(nums, i)
	}
	fmt.Println("nums = ", nums)

	// delete
	m := make(map[string]string)
	m["a"] = "A"
	m["b"] = "B"
	m["c"] = "C"
	fmt.Println("before delete = ", m)
	delete(m, "b")
	fmt.Println("after delete = ", m)

	// copy
	var numsc []int
	copy(nums, numsc)
	fmt.Println("numsc = ", nums)

	numsn := make([]int, 10)
	numsn[0] = 1

	//cap
	fmt.Println("nums cap = ", cap(nums))
	fmt.Println("numsn cap = ", cap(numsn))

	//len
	fmt.Println("nums len = ", len(nums))
	fmt.Println("numsn len = ", len(numsn))

}
