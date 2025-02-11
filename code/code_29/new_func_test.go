package code_29

import (
	"fmt"
	"maps"
	"slices"
	"testing"
)

func TestMax(t *testing.T) {
	oldFunc := func(a, b int) (int, int) {
		maxValue := a
		if a < b {
			maxValue = b
		}
		minValue := a
		if a > b {
			minValue = b
		}
		return maxValue, minValue
	}

	newFunc := func(i int, j int) (int, int) {
		maxValue := max(i, j)
		minValue := min(i, j)
		return maxValue, minValue
	}

	fmt.Println(oldFunc(1, 2))
	fmt.Println(newFunc(1, 4))
}

func TestSliceMax(t *testing.T) {
	oldFunc := func(s []int) (int, int) {
		maxValue := s[0]
		for i := 1; i < len(s); i++ {
			maxValue = max(maxValue, s[i])
		}

		minValue := s[0]
		for i := 1; i < len(s); i++ {
			minValue = min(minValue, s[i])
		}
		return maxValue, minValue
	}

	newFunc := func(s []int) (int, int) {
		maxValue := slices.Max(s)
		minValue := slices.Min(s)
		return maxValue, minValue
	}

	fmt.Println(oldFunc([]int{1, 2, 3, 4, 5}))
	fmt.Println(newFunc([]int{1, 2, 3, 4, 5}))
}

func TestMapToSlice(t *testing.T) {
	oldFunc := func(m map[string]string) ([]string, []string) {
		keys := make([]string, 0, len(m))
		for key := range m {
			keys = append(keys, key)
		}

		values := make([]string, 0, len(m))
		for _, value := range m {
			values = append(values, value)
		}
		return keys, values
	}

	newFunc := func(m map[string]string) ([]string, []string) {
		keys := slices.Collect(maps.Keys(m))
		values := slices.Collect(maps.Values(m))
		return keys, values
	}

	fmt.Println(oldFunc(map[string]string{"a": "1", "b": "2"}))
	fmt.Println(newFunc(map[string]string{"a": "1", "b": "2"}))
}

func TestMapMerge(t *testing.T) {
	oldFunc := func(m1, m2 map[string]string) map[string]int {
		src := map[string]int{"a": 1, "b": 2}
		dst := map[string]int{"c": 3, "d": 4}
		for k, v := range src {
			dst[k] = v
		}
		return dst
	}

	newFunc := func(m1, m2 map[string]string) map[string]int {
		src := map[string]int{"a": 1, "b": 2}
		dst := map[string]int{"c": 3, "d": 4}
		maps.Insert(dst, maps.All(src))
		return dst
	}

	fmt.Println(oldFunc(map[string]string{"a": "1", "b": "2"}, map[string]string{"c": "3", "d": "4"}))
	fmt.Println(newFunc(map[string]string{"a": "1", "b": "2"}, map[string]string{"c": "3", "d": "4"}))
}
