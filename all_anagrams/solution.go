package main

import (
	"fmt"
)

func isAnagram(counter1, counter2 map[string]int) bool {
	for k, v2 := range counter2 {
		v1, ok := counter1[k]
		if ok {
			if v1 != v2 {
				return false
			}
		} else {
			return false
		}
	}
	return true
}

func findAnagrams(s string, p string) []int {
	n, m := len(s), len(p)
	if n < m {
		return []int{}
	}

	pCounter := make(map[string]int)
	for _, c := range p {
		pCounter[string(c)]++
	}

	sCounter := make(map[string]int)
	for _, c := range s[:m] {
		sCounter[string(c)]++
	}

	result := make([]int, 0)

	var prevChar, lastChar string
	if isAnagram(sCounter, pCounter) {
		result = append(result, 0)
		prevChar = string(s[0])
	}

	sCounter[string(s[0])]--

	for i := 1; i <= n-m; i++ {
		lastChar = string(s[i+m-1])

		if prevChar == lastChar {
			result = append(result, i)
			prevChar = string(s[i])
			sCounter[lastChar]++
			sCounter[prevChar]--
			continue
		}

		sCounter[string(lastChar)]++
		if isAnagram(sCounter, pCounter) {
			result = append(result, i)
			prevChar = string(s[i])
		} else {
			prevChar = ""
		}

		sCounter[string(s[i])]--

	}

	return result

}

func main() {
	s := "abababbbb"
	p := "ab"

	fmt.Println(findAnagrams(s, p))
}
