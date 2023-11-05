package main

import "fmt"

func main() {
	m := make(map[string]string)
	m["A"] = "a"
	m["B"] = "b"
	m["C"] = "c"
	m["D"] = "d"
	m["E"] = "e"
	for i := range m {
		fmt.Println(i)
	}
}
