package code_26

import (
	"crypto/sha256"
	"fmt"
	"io"
	"os"
	"testing"
)

func CalculateFileHash(filePath string) (string, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return "", err
	}
	defer func() {
		_ = file.Close()
	}()

	hash := sha256.New()
	if _, err := io.Copy(hash, file); err != nil {
		return "", err
	}

	hashInBytes := hash.Sum(nil)[:32] // SHA-256 produces a 32 byte hash
	return fmt.Sprintf("%x", hashInBytes), nil
}

func TestCalculateFileHash(t *testing.T) {
	hash, err := CalculateFileHash("hello.go")
	if err != nil {
		t.Error(err)
	}
	fmt.Println(hash)
}
