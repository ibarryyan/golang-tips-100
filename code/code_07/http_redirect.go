package code_07

import (
	"log"
	"net/http"
	"testing"
)

func login(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Cache-Control", "must-revalidate, no-store")
	w.Header().Set("Content-Type", " text/html;charset=UTF-8")
	w.Header().Set("Location", "http://www.baidu.com/") //跳转地址设置
	w.WriteHeader(http.StatusFound)
}

func TestResponseHeader(t *testing.T) {
	http.HandleFunc("/", login)
	if err := http.ListenAndServe(":8080");err!= nil {
		log.Fatal("ListenAndServe: ", err)
	}
}

//func login(w http.ResponseWriter, r *http.Request) {
//	w.Redirect(http.StatusFound, "http://www.baidu.com/")
//}
//
//func TestResponseHeader(t *testing.T) {
//	http.HandleFunc("/", login)
//	if err := http.ListenAndServe(":8080");err!= nil {
//		log.Fatal("ListenAndServe: ", err)
//	}
//}