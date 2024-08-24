package code_21

import (
	"errors"
	"fmt"
	"testing"
)

var myErr = errors.New("my err")

func TestError(t *testing.T) {
	err := fmt.Errorf("hello %w", myErr)

	fmt.Printf("myErr:%s , err:%s \n", myErr, err)

	fmt.Println("使用 == 的结果:", err == myErr)
	fmt.Println("使用 errors.Is(err, myErr) 的结果:", errors.Is(err, myErr))
	fmt.Println("使用 errors.Is(myErr, err) 的结果:", errors.Is(myErr, err))
}