package code_40

import (
	"context"
	"fmt"
	"log"
	"sync"

	"golang.org/x/sync/errgroup"
)

func safeGoroutine() {
	defer func() {
		if r := recover(); r != nil {
			log.Printf("Recovered panic: %v\n", r)
			// 执行清理操作
		}
	}()

	// 协程业务逻辑
	// ...
}

func worker(errCh chan<- error) {
	defer func() {
		if r := recover(); r != nil {
			errCh <- fmt.Errorf("panic occurred: %v", r)
		}
	}()

	// 业务逻辑
	//if err := criticalOperation(); err != nil {
	//    errCh <- err
	//}
}

func main() {
	errCh := make(chan error, 1)
	go worker(errCh)

	if err := <-errCh; err != nil {
		log.Fatal("Worker failed:", err)
	}
}

type SafeWaitGroup struct {
	sync.WaitGroup
	errChan chan error
}

func (swg *SafeWaitGroup) Go(f func() error) {
	swg.Add(1)
	go func() {
		defer swg.Done()
		defer func() {
			if r := recover(); r != nil {
				swg.errChan <- fmt.Errorf("panic: %v", r)
			}
		}()

		if err := f(); err != nil {
			swg.errChan <- err
		}
	}()
}

// 使用示例
func main2() {
	swg := &SafeWaitGroup{errChan: make(chan error, 10)}

	swg.Go(func() error { /* ... */ return nil })
	swg.Go(func() error { /* ... */ return nil })

	go func() {
		swg.Wait()
		close(swg.errChan)
	}()

	for err := range swg.errChan {
		log.Println("Error:", err)
	}
}

func main3() {
	g, ctx := errgroup.WithContext(context.Background())

	g.Go(func() error {
		defer func() {
			if r := recover(); r != nil {
				// 将 panic 转换为错误
				return
			}
		}()
		return operation1(ctx)
	})

	g.Go(func() error {
		return operation2(ctx)
	})

	if err := g.Wait(); err != nil {
		log.Fatal("Failed:", err)
	}
}

func operation1(ctx context.Context) error {
	return nil
}

func operation2(ctx context.Context) error {
	return nil
}
