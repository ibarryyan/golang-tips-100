package code_24

import (
    "fmt"
    "testing"
)

func TestInterface(t *testing.T) {
    var i interface{} = "hello"

    // 类型开关
    switch v := i.(type) {
    case int:
        fmt.Println("i is an int:", v)
    case string:
        fmt.Println("i is a string:", v)
    case bool:
        fmt.Println("i is a bool:", v)
    default:
        fmt.Println("i is of a different type")
    }
}
