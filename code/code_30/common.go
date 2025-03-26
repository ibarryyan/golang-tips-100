package code_30

import (
	"fmt"
	"go/ast"
	"go/parser"
	"go/token"
)

func main() {
	// 创建文件集
	fset := token.NewFileSet()

	// 解析当前文件
	f, err := parser.ParseFile(fset, "main.go", nil, parser.ParseComments)
	if err != nil {
		panic(err)
	}

	// 遍历AST节点
	ast.Inspect(f, func(n ast.Node) bool {
		// 查找函数声明
		fn, ok := n.(*ast.FuncDecl)
		if ok && fn.Name.Name == "TestFunc" {
			// 打印函数注释
			if fn.Doc != nil {
				for _, comment := range fn.Doc.List {
					fmt.Println(comment.Text)
				}
			}
		}
		return true
	})
}

// TestFunc
// @param null
// @return error
// @return int
func TestFunc() {

}
