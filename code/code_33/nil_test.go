package code_33

import (
	"fmt"
	"testing"
)

var (
	p *int        // nil pointer
	s []int       // nil slice
	m map[int]int // nil map
	f func()      // nil function
	i interface{} // nil interface
)

func TestNil(t *testing.T) {
	var p *int = nil
	fmt.Println(p == nil) // true
	fmt.Println(i == p)   // false!
}
