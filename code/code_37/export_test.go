package code_37

import (
	"encoding/json"
	"fmt"
)

type Person struct {
	Name string `json:"name"` // 可导出，会被序列化
	age  int    `bson:"age"`  // 非导出，会被忽略
}

func main() {
	// 序列化
	p := Person{Name: "Alice", age: 30}
	jsonData, _ := json.Marshal(p)
	fmt.Println(string(jsonData)) // 输出: {"Name":"Alice"}

	// 反序列化
	var p2 Person
	_ = json.Unmarshal([]byte(`{"Name":"Bob","age":40}`), &p2)
	fmt.Printf("%+v\n", p2) // 输出: {Name:Bob age:0}
}
