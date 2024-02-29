package main

import "testing"

func TestEmptyMap(t *testing.T) {
	var m map[string]struct{}
	m["name"] = struct{}{}
}
