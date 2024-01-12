package code_05

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	group := sync.WaitGroup{}
	group.Add(3)

	for i := 0; i < 3; i++ {
		go func() {
			fmt.Println("hello...")
			group.Done()
		}()
	}

	group.Wait()
}

type Pool struct {
	queue chan int
	wg    *sync.WaitGroup
}

func New(size int) *Pool {
	if size <= 0 {
		size = 1
	}
	return &Pool{
		queue: make(chan int, size),
		wg:    &sync.WaitGroup{},
	}
}

func (p *Pool) Add(delta int) {
	for i := 0; i < delta; i++ {
		p.queue <- 1
	}
	for i := 0; i > delta; i-- {
		<-p.queue
	}
	p.wg.Add(delta)
}

func (p *Pool) Done() {
	<-p.queue
	p.wg.Done()
}

func (p *Pool) Wait() {
	p.wg.Wait()
}

func main1() {
	pool := New(10)
	for i := 0; i < 100; i++ {
		pool.Add(1)
		go func() {
			time.Sleep(time.Second)
			fmt.Printf("%d hello...\n", i)
			pool.Done()
		}()
	}
	pool.Wait()
}
