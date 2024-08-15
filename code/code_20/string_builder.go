package code_20

import (
	"fmt"
	"strings"
	"testing"
)

const (
	hello = "Hello "
	world = "World"
	sign  = "!"
)

// 推荐
func userBuilder() string {
	builder := strings.Builder{}
	builder.WriteString(hello)
	builder.WriteString(world)
	builder.WriteString(sign)
	return builder.String()
}

// 不太推荐
func userPlus() string {
	return hello + world + sign
}

// 很不推荐
func userFmt() string {
	return fmt.Sprintf("%s%s%s", hello, world, sign)
}
