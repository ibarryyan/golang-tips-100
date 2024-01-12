package code_06

import (
	"fmt"
	"net/http"
	_ "net/http/pprof"
)

func main() {
	ints := make(chan int, 1000)
	i := 0

	worker := func(ch chan int) {
		for v := range ch {
			fmt.Println(v)
		}
	}

	http.HandleFunc("/go", func(writer http.ResponseWriter, request *http.Request) {
		i += 1
		ints <- i
		go worker(ints)
	})
	http.ListenAndServe(":9090", nil)
}

//------------

func main() {
	ints := make(chan int, 1000)
	i := 0

	worker := func(ch chan int) {
		select {
		case v := <-ch:
			fmt.Println(v)
		default:
			return
		}
	}

	http.HandleFunc("/go", func(writer http.ResponseWriter, request *http.Request) {
		i += 1
		ints <- i
		go worker(ints)
	})
	http.ListenAndServe(":9090", nil)
}

//------------

func worker(v ...int) {
	count := len(v)
	res := make(chan int, count)

	go func(ch chan int) {
		for i := 0; i < count; i++ {
			fmt.Println(v[i])
			ch <- v[i]
		}
	}(res)

	for i := 0; i < count; i++ {
		<-res
	}

	close(res)
}

func main() {
	val := 0

	http.HandleFunc("/go", func(writer http.ResponseWriter, request *http.Request) {
		val += 1
		go worker(val)
	})
	http.ListenAndServe(":9090", nil)
}
