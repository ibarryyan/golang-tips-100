package code_08

import "fmt"

type Student struct {
	Name string
}

func main() {
	var stu Student
	fmt.Println(stu.Name)

	var stuP *Student

	stuP = &Student{} //如不进行赋值则会报错

	fmt.Println(stuP.Name)
}
