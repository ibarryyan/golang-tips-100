package code_27

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var a int
	var b string
	fmt.Print("Enter an integer and a string separated by space: ")
	fmt.Scan(&a, &b)
	fmt.Println("You entered:", a, b)
}

func main2() {
	var name string
	var age int
	fmt.Print("Enter your name and age (e.g., Alice 30): ")
	fmt.Scanf("%s %d", &name, &age)
	fmt.Println("Hello,", name, "you are", age, "years old.")
}

func main3() {
	var a int
	var b string
	fmt.Print("Enter an integer and a string on the same line: ")
	fmt.Scanln(&a, &b)
	fmt.Println("You entered:", a, b)
}

func main4() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords) // 设置分隔符为空格
	fmt.Println("Enter some words (type 'exit' to quit):")
	for scanner.Scan() {
		word := scanner.Text()
		if strings.ToLower(word) == "exit" {
			break
		}
		fmt.Println("You entered:", word)
	}
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading input:", err)
	}
}
