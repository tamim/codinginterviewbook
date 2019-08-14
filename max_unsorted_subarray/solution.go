package main

import "fmt"

func main() {
	A := []int{4, 5, 7, 9, 1, 3, 8, 20, 18}
	fmt.Println(subUnsort(A))

	A = []int{4, 5, 7, 9, 1, 3, 8, 10, 18}
	fmt.Println(subUnsort(A))

	A = []int{4, 5, 7, 9, 1, 3, 8, 20, 18, 22, 23}
	fmt.Println(subUnsort(A))
}

func subUnsort(A []int) []int {
	var min, max, start, end, i, n int

	n = len(A)

	for i = 0; i < n-1; i++ {
		if A[i] > A[i+1] {
			break
		}
	}
	if i == n-1 {
		return []int{-1}
	}

	start = i

	for i = n - 1; i > start; i-- {
		if A[i] < A[start] || A[i] < A[i-1] {
			break
		}
	}
	end = i

	min = A[start]
	max = A[start]

	for i = start; i <= end; i++ {
		if A[i] < min {
			min = A[i]
		}
		if A[i] > max {
			max = A[i]
		}
	}

	for i = 0; i < start; i++ {
		if A[i] > min {
			start = i
			break
		}
	}

	for i = n - 1; i > end; i-- {
		if A[i] < max {
			end = i
			break
		}
	}

	return []int{start, end}
}
