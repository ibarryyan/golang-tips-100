package code_10

import (
	"fmt"
	"testing"
)

func TestStrLen(t *testing.T) {
	s1 := "123321"
	fmt.Println(len(s1)) // 6

	s2 := "一二三"
	fmt.Println(len(s2)) // 9

	s3 := []rune("一二三")
	fmt.Println(len(s3)) // 3
}
