package code_39

import (
	"sync/atomic"
	"unsafe"
)

//1） 实现自旋锁

type SpinLock struct {
	state *int32 // 0=unlocked, 1=locked
}

func (s *SpinLock) Lock() {
	// 循环尝试直到成功
	for !atomic.CompareAndSwapInt32(s.state, 0, 1) {
		// 可加入 runtime.Gosched() 减少CPU消耗
	}
}

func (s *SpinLock) Unlock() {
	atomic.StoreInt32(s.state, 0)
}

//2）实现原子计数器

type AtomicCounter struct {
	value int32
}

func (c *AtomicCounter) Increment() int32 {
	for {
		old := atomic.LoadInt32(&c.value)
		new := old + 1
		if atomic.CompareAndSwapInt32(&c.value, old, new) {
			return new
		}
	}
}

//3）实现无锁队列

type Node struct {
	value interface{}
	next  *Node
}

type LockFreeQueue struct {
	head *Node
	tail *Node
}

func (q *LockFreeQueue) Enqueue(value interface{}) {
	newNode := &Node{value: value}

	for {
		tail := atomic.LoadPointer((*unsafe.Pointer)(unsafe.Pointer(&q.tail)))
		next := (*Node)(tail).next

		// 确保tail没有被其他goroutine修改
		if tail == atomic.LoadPointer((*unsafe.Pointer)(unsafe.Pointer(&q.tail))) {
			if next == nil {
				// 尝试插入新节点
				if atomic.CompareAndSwapPointer(
					(*unsafe.Pointer)(unsafe.Pointer(&(*Node)(tail).next)),
					nil,
					unsafe.Pointer(newNode)) {
					// 更新tail指针
					atomic.CompareAndSwapPointer(
						(*unsafe.Pointer)(unsafe.Pointer(&q.tail)),
						tail,
						unsafe.Pointer(newNode))
					return
				}
			} else {
				// 帮助其他goroutine完成操作
				atomic.CompareAndSwapPointer(
					(*unsafe.Pointer)(unsafe.Pointer(&q.tail)),
					tail,
					unsafe.Pointer(next))
			}
		}
	}
}
