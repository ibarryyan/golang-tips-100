package code_35

import "fmt"

type B struct {
	Name string
	Say  Say
}

type Hi interface {
	Hi()
}

func (b *B) Hi() {
	fmt.Println("Hi ", b.Name)
}

func NewB(name string) *B {
	return &B{
		Name: name,
		Say:  NewA("A"),
	}
}
