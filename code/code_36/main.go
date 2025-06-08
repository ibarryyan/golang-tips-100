package code_36

import (
	"embed"
	"fmt"
)

// 嵌入单个文件
//
//go:embed assets/config.json
var configFile []byte

// 嵌入整个目录
//
//go:embed assets/*
var assetsFS embed.FS

func main() {
	// 读取单个文件内容
	fmt.Println("Config Content:", string(configFile))

	// 读取目录中的文件
	data, err := assetsFS.ReadFile("assets/config.json")
	if err != nil {
		panic(err)
	}
	fmt.Println("Data File Size:", len(data))

	// 遍历目录（Go 1.16+）
	entries, _ := assetsFS.ReadDir("assets")
	for _, entry := range entries {
		fmt.Println("Found:", entry.Name())
	}
}

func swap(a, b *int) {
	*a, *b = *b, *a // 通过指针解引用交换值
}

func main2() {
	m, n := 30, 40
	swap(&m, &n)
	fmt.Println(m, n) // 输出: 40 30
}

func main1() {
	x, y := 5, 15
	fmt.Printf("交换前: x=%d, y=%d\n", x, y) // 输出: x=5, y=15

	x, y = y, x                           // 核心交换操作
	fmt.Printf("交换后: x=%d, y=%d\n", x, y) // 输出: x=15, y=5
}
