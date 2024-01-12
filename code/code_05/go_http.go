package code_05

import (
	"fmt"
	"io"
	"net/http"
	"net/url"
	"strconv"
)

type Student struct {
	Name string
	Age  int
}

func HttpServe() {
	http.HandleFunc("/get", func(w http.ResponseWriter, r *http.Request) {
		str := r.URL.Query().Get("str")
		fmt.Println("Get Method Str is " + str)
		w.Write([]byte("Hello Http Get!"))
	})

	http.HandleFunc("/get/form", func(w http.ResponseWriter, r *http.Request) {
		name := r.URL.Query().Get("name")
		age := r.URL.Query().Get("age")
		ageStr, err := strconv.Atoi(age)
		if err != nil {
			fmt.Println("err...")
		}
		stu := Student{Name: name, Age: ageStr}
		fmt.Println("Get Method Str is ", stu)
		w.Write([]byte("Hello Http Get Form!"))
	})

	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Println(err)
	}
}

func HttpGet() {
	resp, err := http.Get("http://localhost:8080/get?str=ymx") // url
	if err != nil {
		fmt.Printf("get请求失败 error: %+v", err)
		return
	}
	defer resp.Body.Close()
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("读取Body失败 error: %+v", err)
		return
	}
	fmt.Println(string(body))
}

func HttpPost() {
	resp, err := http.PostForm("http://localhost:8080/form",
		url.Values{
			"name": {"jack"},
		})
	if err != nil {
		fmt.Printf("postForm请求失败 error: %+v", err)
		return
	}
	defer resp.Body.Close()
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("读取Body失败 error: %+v", err)
		return
	}
	fmt.Println(string(body))
}
