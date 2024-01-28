package code_07

import (
	"io"
	"log"
	"os"
	"testing"
)

func TestPrintLogToFile(t *testing.T) {
	f, err := os.OpenFile("log.log", os.O_CREATE|os.O_APPEND|os.O_RDWR, os.ModePerm)
	if err != nil {
		return
	}
	defer func() {
		f.Close()
	}()

	multiWriter := io.MultiWriter(os.Stdout, f)
	log.SetOutput(multiWriter)

	log.SetFlags(log.Ldate | log.Ltime | log.Lshortfile)

	log.Println("log1")
	log.Print("log222")
	log.Printf("line%d \n", 171)
}
