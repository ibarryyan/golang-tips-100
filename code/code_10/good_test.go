package code_10

import "testing"

func TestAdd(t *testing.T) {
	// Define the test table
	tests := []struct {
		name   string
		inputA int
		inputB int
		want   int
	}{
		{"Add 1 and 2", 1, 2, 3},
		{"Add -1 and 1", -1, 1, 0},
		// Add more test cases here
	}

	// Iterate over the test table
	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			got := Add(tc.inputA, tc.inputB)
			if got != tc.want {
				t.Errorf("Add(%d, %d) = %d; want %d", tc.inputA, tc.inputB, got, tc.want)
			}
		})
	}
}

func Add(a int, b int) int {
	return a + b
}
