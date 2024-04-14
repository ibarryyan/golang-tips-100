package main

import (
	"code/code_14/db"
	"fmt"
)

func init() {
	fmt.Println("package main init() func ...")
}

func main() {
	db.LoadModel() //顺序调换还是限制性另一个文件的init函数
	db.LoadConfig()
	fmt.Println("package main main() func ...")
}
