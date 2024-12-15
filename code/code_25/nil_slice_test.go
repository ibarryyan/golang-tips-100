package code_25

import (
	"fmt"
	"reflect"
	"testing"
	"unsafe"
)

func TestNilSlice(t *testing.T) {
	var s1 []int
	s2 := make([]int, 0)
	s3 := make([]int, 0)

	fmt.Printf("s1 pointer:%+v \ns2 pointer:%+v \ns3 pointer:%+v, \n",
		*(*reflect.SliceHeader)(unsafe.Pointer(&s1)),
		*(*reflect.SliceHeader)(unsafe.Pointer(&s2)),
		*(*reflect.SliceHeader)(unsafe.Pointer(&s3)))
	fmt.Printf("%v\n",
		(*(*reflect.SliceHeader)(unsafe.Pointer(&s1))).Data == (*(*reflect.SliceHeader)(unsafe.Pointer(&s2))).Data)
	fmt.Printf("%v\n",
		(*(*reflect.SliceHeader)(unsafe.Pointer(&s2))).Data == (*(*reflect.SliceHeader)(unsafe.Pointer(&s3))).Data)
}
