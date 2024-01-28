package code_08

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

func main() {
	defer func() {
		fmt.Println("defer func ...")
	}()

	fmt.Println("main func ...")

	ch := make(chan os.Signal, 1)

	signal.Notify(ch, syscall.SIGTERM, syscall.SIGQUIT, syscall.SIGINT)

	sig := <-ch

	fmt.Printf("get signal %+v ...\n", sig)
}

