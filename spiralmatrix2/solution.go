package main

import "fmt"

func generateMatrix(n int) [][]int {
	var left, right, top, bottom, i int

	matrix := make([][]int, n)
	for i = 0; i < n; i++ {
		matrix[i] = make([]int, n)
	}

	right = n - 1
	bottom = n - 1

	num := 1

	direction := 0

	for left <= right && top <= bottom {
		if direction == 0 {
			for i = left; i <= right; i++ {
				matrix[top][i] = num
				num++
			}
			top++
		} else if direction == 1 {
			for i = top; i <= bottom; i++ {
				matrix[i][right] = num
				num++
			}
			right--
		} else if direction == 2 {
			for i = right; i >= left; i-- {
				matrix[bottom][i] = num
				num++
			}
			bottom--
		} else {
			for i = bottom; i >= top; i-- {
				matrix[i][left] = num
				num++
			}
			left++
		}

		direction = (direction + 1) % 4
	}

	return matrix
}

func main() {
	n := 3
	fmt.Println(generateMatrix(n))
}
