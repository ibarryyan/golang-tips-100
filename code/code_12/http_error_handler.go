package main

import (
	"fmt"
	"log"
	"net/http"
)

// 全局异常处理器
func globalErrorHandler(err error, w http.ResponseWriter, r *http.Request) {
	// 记录错误信息
	log.Printf("Error: %v", err)

	// 设置HTTP状态码
	if httpErr, ok := err.(*http.Error); ok {
		w.WriteHeader(httpErr.Code)
	} else {
		w.WriteHeader(http.StatusInternalServerError)
	}

	// 返回错误消息给客户端
	w.Write([]byte(err.Error()))
}

// 自定义HTTP错误处理函数
func handleError(w http.ResponseWriter, r *http.Request, err error) {
	// 在这里你可以根据需要对错误进行特殊处理
	// 如果没有特殊处理，则调用全局异常处理器
	globalErrorHandler(err, w, r)
}

// 示例HTTP处理函数
func helloHandler(w http.ResponseWriter, r *http.Request) {
	// 示例：故意制造一个错误
	panic("Something went wrong!")
}

func main() {
	// 设置自定义错误处理函数
	http.DefaultServeMux.HandleFunc("/", helloHandler)
	http.DefaultServeMux.HandleFunc("/healthz", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("OK"))
	})

	// 使用自定义错误处理函数作为全局异常处理器
	http.DefaultServeMux.HandlerFunc("/global-error-handler").Func = func(w http.ResponseWriter, r *http.Request) {
		defer func() {
			if err := recover(); err != nil {
				handleError(w, r, err)
			}
		}()
		http.NotFound(w, r)
	}

	fmt.Println("Server is running at http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
