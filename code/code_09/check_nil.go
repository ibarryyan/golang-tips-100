package code_09

import (
	"fmt"
	"io/ioutil"
	"os"
)

func readFile(filename string) (content string, err error) {
	file, err := os.Open(filename)
	if err != nil {
		return "", err
	}
	defer file.Close()

	data, err := ioutil.ReadAll(file)
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func printLength(s *string) {
	if s == nil {
		fmt.Println("Received a nil string pointer!")
		return
	}
	fmt.Printf("String length is: %d\n", len(*s))
}
