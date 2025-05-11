package code_33

import (
	"bytes"
	"encoding/json"
	"sync"
)

var bufferPool = sync.Pool{
	New: func() interface{} { return new(bytes.Buffer) },
}

func EncodeJSON(v interface{}) ([]byte, error) {
	buf := bufferPool.Get().(*bytes.Buffer)
	defer bufferPool.Put(buf)
	buf.Reset() // 关键：清空旧数据
	err := json.NewEncoder(buf).Encode(v)
	return buf.Bytes(), err
}
