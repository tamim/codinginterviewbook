// https://leetcode.com/problems/valid-anagram/

package main

import (
	"fmt"
	"sort"
	"strings"
)

func sortString1(s string) string {
	a := strings.Split(s, "")
	sort.Strings(a)
	return strings.Join(a, "")
}

type sortRunes []rune

func (s sortRunes) Less(i, j int) bool {
	return s[i] < s[j]
}

func (s sortRunes) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s sortRunes) Len() int {
	return len(s)
}

func sortString2(s string) string {
	r := []rune(s)
	sort.Sort(sortRunes(r))
	return string(r)
}

func isAnagram(s string, t string) bool {
	s = sortString1(s)
	t = sortString1(t)

	return s == t
}

func isAnagram2(s string, t string) bool {
	sLen, tLen := len(s), len(t)
	if sLen != tLen {
		return false
	}

	sCounter := make(map[rune]int)
	for _, c := range s {
		sCounter[c]++
	}

	tCounter := make(map[rune]int)
	for _, c := range t {
		tCounter[c]++
	}

	for k, v := range sCounter {
		v2, ok := tCounter[k]
		if !ok || v != v2 {
			return false
		}
	}

	return true
}

func main() {
	s := "anagram"
	t := "gramama"

	fmt.Println(isAnagram2(s, t))
}
