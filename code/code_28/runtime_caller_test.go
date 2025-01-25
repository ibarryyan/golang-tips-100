package code_28

import (
	"fmt"
	"runtime"
	"testing"
)

func getCallerInfo() (string, string, int) {
	pc, file, line, ok := runtime.Caller(1)
	if !ok {
		return "", "", 0
	}
	funcName := runtime.FuncForPC(pc).Name()
	return funcName, file, line
}

func TestCallerInfo(t *testing.T) {
	funcName, file, line := getCallerInfo()
	fmt.Printf("func name: %s \n", funcName)
	fmt.Printf("call file: %s \n", file)
	fmt.Printf("code line: %d \n", line)
}
