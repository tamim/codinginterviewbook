package main

import "fmt"

func spiralOrder(A [][]int) []int {
	m := len(A)
	if m == 0 {
		return []int{}
	}
	n := len(A[0])

	result := make([]int, m*n)
	indx := 0

	left := 0
	right := n - 1
	top := 0
	bottom := m - 1

	direction := 0

	var i int

	for top <= bottom && left <= right {
		if direction == 0 {
			for i = left; i <= right; i++ {
				result[indx] = A[top][i]
				indx++
			}
			top++
		} else if direction == 1 {
			for i = top; i <= bottom; i++ {
				result[indx] = A[i][right]
				indx++
			}
			right--
		} else if direction == 2 {
			for i = right; i >= left; i-- {
				result[indx] = A[bottom][i]
				indx++
			}
			bottom--
		} else { // direction 3
			for i = bottom; i >= top; i-- {
				result[indx] = A[i][left]
				indx++
			}
			left++
		}

		direction = (direction + 1) % 4
	}

	return result
}

func main() {
	matrix := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	result := spiralOrder(matrix)
	fmt.Println(result)
}
