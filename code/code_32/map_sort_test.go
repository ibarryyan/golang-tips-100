package code_32

import (
	"fmt"
	"sort"

	"github.com/emirpasic/gods/maps/treemap"
)

type OrderedMap struct {
	items map[interface{}]interface{}
	order []interface{}
}

func NewOrderedMap() *OrderedMap {
	return &OrderedMap{
		items: make(map[interface{}]interface{}),
		order: make([]interface{}, 0),
	}
}

func (m *OrderedMap) Set(key, value interface{}) {
	if _, exists := m.items[key]; !exists {
		m.order = append(m.order, key)
	}
	m.items[key] = value
}

func (m *OrderedMap) Get(key interface{}) (interface{}, bool) {
	val, exists := m.items[key]
	return val, exists
}

func (m *OrderedMap) Delete(key interface{}) {
	delete(m.items, key)
	// 重建顺序切片（简单实现，实际可用更高效方式）
	newOrder := make([]interface{}, 0, len(m.order)-1)
	for _, k := range m.order {
		if k != key {
			newOrder = append(newOrder, k)
		}
	}
	m.order = newOrder
}

func (m *OrderedMap) Iterate() {
	for _, key := range m.order {
		fmt.Printf("%v: %v\n", key, m.items[key])
	}
}

// ---

type SortedMap struct {
	keys  []int
	items map[int]string
}

func NewSortedMap() *SortedMap {
	return &SortedMap{
		keys:  make([]int, 0),
		items: make(map[int]string),
	}
}

func (m *SortedMap) Set(key int, value string) {
	if _, exists := m.items[key]; !exists {
		m.keys = append(m.keys, key)
		sort.Ints(m.keys) // 保持有序
	}
	m.items[key] = value
}

func (m *SortedMap) Get(key int) (string, bool) {
	val, exists := m.items[key]
	return val, exists
}

func (m *SortedMap) Iterate() {
	for _, key := range m.keys {
		fmt.Printf("%d: %s\n", key, m.items[key])
	}
}

//---

func main() {
	// 自然排序
	m := treemap.NewWithIntComparator()
	m.Put(1, "one")
	m.Put(3, "three")
	m.Put(2, "two")

	// 迭代器
	it := m.Iterator()
	for it.Next() {
		fmt.Printf("%d: %s\n", it.Key(), it.Value())
	}

	// 反向迭代
	rit := m.Iterator()
	for rit.Next() {
		fmt.Printf("%d: %s\n", rit.Key(), rit.Value())
	}
}
