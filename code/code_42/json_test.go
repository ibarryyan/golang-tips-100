package code_42

import (
	"encoding/json"
	"fmt"
	"testing"
)

func TestJson(t *testing.T) {
	var m map[string]interface{}
	data := []byte(`{"id": 9223372036854775807}`)
	_ = json.Unmarshal(data, &m)
	fmt.Println(m["id"]) // 输出 9.223372036854776e+18 (float64)，精度丢失
}
