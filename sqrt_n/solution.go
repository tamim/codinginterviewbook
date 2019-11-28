package main

import (
	"fmt"
	"math"
)

func sqrtN(n float64) float64 {
	delta := float64(0.00000001)

	left := float64(0.0)
	right := n

	var mid, m, diff float64

	for left < right {
		mid = (left + right) / 2.0

		m = mid * mid
		diff = math.Abs(m - n)
		if diff < delta {
			return mid
		}

		if m > n {
			right = mid
		} else {
			left = mid
		}
	}

	return mid
}

func main() {
	var n int64

	n = 9

	if n < 0 {
		fmt.Println("The number can't be negative")
	} else {
		root := sqrtN(float64(n))
		fmt.Println(root)
	}
}
