package main

import (
	"fmt"
	"strings"
)

func minCharsToPalindrome(s string) int {
	l := len(s)
	if l == 1 {
		return 0
	}

	// check if it's arleady a palindrome
	i := 0
	j := l - 1
	for ; i < j; i++ {
		if s[i] != s[j] {
			break
		}
		j--
	}
	if i >= j {
		return 0 // palindrome
	}

	for m := int((l-1)/2) - 1; m >= 0; m-- {
		for r := m + 2; r >= m+1; r-- {
			i := m
			j := r
			for ; i >= 0; i-- {
				if s[i] != s[j] {
					break
				}
				j++
			}
			if i < 0 {
				return (l - j)
			}
		}
	}

	return l - 1
}

func shortestPalindrome(s string) string {
	n := minCharsToPalindrome(s)
	if n == 0 {
		return s
	}
	l := len(s)
	p := make([]string, 0, n+l)

	i := 0
	for j := l - 1; i < n; i++ {
		p = append(p, string(s[j]))
		j--
	}

	for j := 0; j < l; j++ {
		p = append(p, string(s[j]))
	}

	return strings.Join(p, "")
}

func shortestPalindrome2(s string) string {
	n := minCharsToPalindrome(s)
	if n == 0 {
		return s
	}
	l := len(s)
	p := make([]byte, 0, n+l)

	i := 0
	for j := l - 1; i < n; i++ {
		p = append(p, s[j])
		j--
	}

	for j := 0; j < l; j++ {
		p = append(p, s[j])
	}

	return string(p)
}

func main() {
	s := "abcba"
	fmt.Println(s, shortestPalindrome2(s))

	s = "abba"
	fmt.Println(s, shortestPalindrome2(s))

	s = "abbb"
	fmt.Println(s, shortestPalindrome2(s))

	s = "abbac"
	fmt.Println(s, shortestPalindrome2(s))

	s = "AACECAAAA"
	fmt.Println(s, shortestPalindrome2(s))
}
