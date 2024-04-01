package main

import (
	"fmt"
	"io"
	"math/rand"
	"net"
	"net/http"
	"os"
	"path"
	"path/filepath"
)

const (
	uploadPath    = "tmp"
	maxUploadSize = 10 << 20 //10MB
)

func main() {
	listen, _ := net.Listen("tcp", ":8888")

	//文件上传
	http.HandleFunc("/upload", func(w http.ResponseWriter, r *http.Request) {
		if err := r.ParseMultipartForm(maxUploadSize); err != nil {
			fmt.Printf("ParseMultipartForm err = %s", err)
			return
		}

		file, fileHeader, err := r.FormFile("file")
		if err != nil {
			fmt.Printf("FormFile err = %s", err)
			return
		}

		defer func() {
			_ = file.Close()
		}()

		if fileHeader.Size > maxUploadSize {
			fmt.Printf("max err = %s", err)
			return
		}

		fileBytes, err := io.ReadAll(file)
		if err != nil {
			fmt.Printf("read err = %s", err)
			return
		}

		newFileName := randToken(12) + path.Ext(fileHeader.Filename) //新文件名+后缀
		newFile, err := os.Create(filepath.Join(uploadPath, newFileName))
		if err != nil {
			fmt.Printf("Create err = %s", err)
			return
		}

		defer func() {
			_ = newFile.Close()
		}()

		if _, err := newFile.Write(fileBytes); err != nil || newFile.Close() != nil {
			fmt.Printf("Write err = %s", err)
			return
		}
		_, _ = w.Write([]byte("ok"))
	})

	//文件下载  http://localhost:8888/static/9a621d729566c74d10037c4d.jpg
	http.Handle("/static/", http.FileServer(http.Dir(uploadPath)))

	_ = http.Serve(listen, nil)
}

func randToken(len int) string {
	b := make([]byte, len)
	rand.Read(b)
	return fmt.Sprintf("%x", b)
}
