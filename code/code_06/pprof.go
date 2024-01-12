package code_06

import (
	"net/http"
	_ "net/http/pprof"
)

func main() {
	http.HandleFunc("/", func(writer http.ResponseWriter, request *http.Request) {
		writer.Write([]byte("Hello~"))
	})
	http.ListenAndServe(":9090", nil)
}
