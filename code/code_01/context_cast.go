package main

import (
	"context"
	"fmt"
	"time"
)

func Handler(ctx context.Context) {
	fmt.Println(ctx.Value("name"))
	fmt.Println(ctx.Deadline())
}

func Controller(ctx context.Context) {
	fmt.Println(ctx.Value("name"))
	fmt.Println(ctx.Deadline())
	ctx = context.WithValue(ctx, "name", "ls")
	ctx, _ = context.WithTimeout(ctx, time.Second*10)
	Handler(ctx)
}

func main() {
	ctx := context.WithValue(context.Background(), "name", "zs")
	ctx, _ = context.WithTimeout(ctx, time.Second*5)
	Controller(ctx)
}
