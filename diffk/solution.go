package main

import "fmt"

func binarySearch(ara []int, left, right, key int) int {
	for left <= right {
		mid := (left + right) / 2
		if ara[mid] == key {
			return mid
		}
		if ara[mid] < key {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return -1
}

func diffPossible1(ara []int, k int) bool {
	n := len(ara)
	for i := 0; i < n-1; i++ {
		key := ara[i] + k
		indx := binarySearch(ara, i+1, n-1, key)
		if indx != -1 {
			return true
		}
	}

	return false
}

func diffPossible2(ara []int, k int) bool {
	n := len(ara)

	for i, j := 0, 1; i < n-1 && j < n; {
		diff := ara[j] - ara[i]
		if diff == k {
			return true
		}
		if diff < k {
			j++
		} else {
			i++
		}
	}

	return false
}

func main() {
	ara := []int{3, 3, 4, 5, 5, 6, 6, 7, 7, 7, 9, 14}
	k := 5

	fmt.Println(diffPossible1(ara, k))
	fmt.Println(diffPossible2(ara, k))

	k = 12
	fmt.Println(diffPossible1(ara, k))
	fmt.Println(diffPossible2(ara, k))
}
