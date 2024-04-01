package main

import (
	"bufio"
	"fmt"
	"io"
	"os/exec"
)

func main() {
	_ = Open("http://localhost:8889")
}

func Open(uri string) error {
	cmd := exec.Command("cmd", "/C", "start "+uri)
	return cmd.Run()
}

// 执行cmd命令
func execCommand(commandName string, params []string) bool {
	cmd := exec.Command(commandName, params...)

	stdout, err := cmd.StdoutPipe()
	if err != nil {
		return false
	}

	if err := cmd.Start(); err != nil {
		panic(err)
	}

	reader := bufio.NewReader(stdout)
	for {
		out, err2 := reader.ReadBytes('\n')
		if err2 != nil || io.EOF == err2 {
			break
		}
		fmt.Println(string(out))
	}
	if err := cmd.Wait(); err != nil {
		panic(err)
	}
	return true
}
