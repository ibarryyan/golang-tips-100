package code_20

import "testing"

func typeCover(t *testing.T) {

	// 不推荐
	var nums []interface{} = [...]interface{}{1, 2, 3, 4}
	for _, num := range nums {
		if v, ok := num.(int); ok {
			fmt.Println(v)
		}
	}

	// 推荐（如果类型已知）
	var nums []int = [...]int{1, 2, 3, 4}
	for _, num := range nums {
		fmt.Println(num)
	}
}
