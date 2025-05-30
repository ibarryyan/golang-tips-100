package code_35

import "fmt"

type A struct {
	Name string
	Hi   Hi
}

type Say interface {
	Say()
}

func (a *A) Say() {
	fmt.Println(a.Name, " say Hi")
}

func NewA(name string) *A {
	return &A{
		Name: name,
		Hi:   NewB("B"),
	}
}
