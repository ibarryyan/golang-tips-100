package code_10

import (
	"fmt"
	"testing"
)

func TestSlice(t *testing.T) {
	arr1 := make([]string, 0)
	arr2 := make([]string, 0)

	arr1 = append(arr1, "A")
	arr1 = append(arr1, "B")
	arr1 = append(arr1, "C")

	arr2 = append(arr2, "a")
	arr2 = append(arr2, "b")
	arr2 = append(arr2, "c")

	fmt.Printf("arr1 = %+v\n", arr1)
	fmt.Printf("arr2 = %+v\n", arr2)

	arr3 := append(arr1, arr2...)
	fmt.Printf("arr3 = %+v\n", arr3)

	arr1p := arr1[:2]
	arr2p := arr2[2:]
	fmt.Printf("arr1p = %+v\n", arr1p)
	fmt.Printf("arr2p = %+v\n", arr2p)

	arr3p := arr3[1:3]
	fmt.Printf("arr3p = %+v\n", arr3p)
}
