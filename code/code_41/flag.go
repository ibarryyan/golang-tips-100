package code_41

import (
	"flag"
	"fmt"
)

func main() {
	var str = flag.String("name", "world", "A string flag")
	flag.Parse()
	fmt.Println(*str)
}
