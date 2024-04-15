package code_15

import "fmt"

type People struct {
	Name string
}

type Student struct {
	People
}

type Say interface {
	SayHello() string
}

//结构体值接收者实现接口
//func (p People) SayHello() string {
// return "hello"
//}

func (p *People) SayHello() string {
	return "hello"
}

func main() {
	people := People{Name: "zs"}

	//student := Student{People: people}  //结构体值定义

	student := &Student{People: people}

	Print(student)
}

func Print(s Say) {
	//student, ok := s.(People) //结构体值断言

	student, ok := s.(*People)
	fmt.Println(ok)
	fmt.Println(student)
}
