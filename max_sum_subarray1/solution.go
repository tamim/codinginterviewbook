package main

import (
	"fmt"
	"math"
)

// https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

// O(n)
func maxSubArray(A []int) int {
	maxSum := math.MinInt32
	currentSum := 0
	n := len(A)
	for i := 0; i < n; i++ {
		currentSum += A[i]
		if currentSum > maxSum {
			maxSum = currentSum
		}
		if currentSum < 0 {
			currentSum = 0
		}
	}

	return maxSum
}

// O(n ^ 2)
func maxSubArray2(A []int) int {
	maxSum := math.MinInt32
	currentSum := 0
	n := len(A)

	for i := 0; i < n; i++ {
		if A[i] > maxSum {
			maxSum = A[i]
		}
		currentSum = A[i]
		for j := i + 1; j < n; j++ {
			currentSum += A[j]
			if currentSum > maxSum {
				maxSum = currentSum
			}
		}
	}

	return maxSum
}

func main() {
	fmt.Println(maxSubArray([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}))  // ans 6
	fmt.Println(maxSubArray2([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4})) // ans 6
}
