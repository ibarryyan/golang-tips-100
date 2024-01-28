package main

import (
	"fmt"
	"testing"
)

type Student struct {
	Id   string
	Name string
}

func TestMapPointKey(t *testing.T) {
	m := make(map[*Student]struct{})

	m[&Student{Id: "1", Name: "zs"}] = struct{}{}

	_, ok := m[&Student{Id: "1", Name: "zs"}]
	fmt.Println(ok)
}

func TestMap(t *testing.T) {
	m := make(map[Student]struct{})

	m[Student{Id: "1", Name: "zs"}] = struct{}{}

	_, ok := m[*&Student{Id: "1", Name: "zs"}]
	fmt.Println(ok)
}

func TestMapInt(t *testing.T) {
	m := make(map[*int]struct{})

	p := 1
	m[&p] = struct{}{}

	p1 := 1
	_, ok := m[&p1]
	fmt.Println(ok) // false

	m2 := make(map[int]struct{})

	p2 := 1
	m2[p2] = struct{}{}

	p3 := 1
	_, ok = m2[p3]
	fmt.Println(ok) // true
}

