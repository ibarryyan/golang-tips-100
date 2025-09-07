package code_42

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"testing"
)

func TestSha256(t *testing.T) {
	data := "hello, go!"

	// 1. 计算 SHA256 哈希，结果是 [32]byte
	hash := sha256.Sum256([]byte(data))

	// 2. 转成字节切片（[]byte）
	// [:] 语法是把数组转成切片
	hashBytes := hash[:]

	// 3. 转成十六进制字符串
	hashString := hex.EncodeToString(hash[:])

	// 4. 直接格式化输出（%x）
	hashFmt := fmt.Sprintf("%x", hash)

	fmt.Println("原始数据:", data)
	fmt.Println("SHA256 数组:", hash)        // [32]byte
	fmt.Println("SHA256 字节切片:", hashBytes) // []byte
	fmt.Println("SHA256 十六进制字符串:", hashString)
	fmt.Println("SHA256 使用 fmt.Sprintf 输出:", hashFmt)
}
