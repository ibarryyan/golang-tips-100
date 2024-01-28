package code_08

import (
	"testing"
	"time"
)

func TestSleep(t *testing.T) {

	<-time.After(time.Second) // 相当于time.Sleep(time.Second)

}
