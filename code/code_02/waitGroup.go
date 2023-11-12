package code_02

import (
	"fmt"
	"sync"
)

func main() {
	group := sync.WaitGroup{}
	group.Add(1)
	go func() {
		defer group.Done()
		fmt.Println("Hello goruntine")
	}()
	fmt.Println("Hello main")
	group.Wait()
}
