package code_15

type Person struct {
	Name string
	Age  int32
}

func (p *Person) AddAge() *Person {
	p.Age++
	return p
}

func (p *Person) Rename(name string) *Person {
	p.Name = name
	return p
}

func main() {
	p := &Person{}
	p = p.AddAge().Rename("ZhangSan")
}
