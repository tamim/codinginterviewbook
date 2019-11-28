package main

import (
	"fmt"
	"regexp"
	"strings"
)

func isNumber(num string) bool {
	num = strings.TrimSpace(num)

	var (
		r1 = regexp.MustCompile(`^[-+]?\d+$`)
		r2 = regexp.MustCompile(`^[-+]?(\d+)?\.\d+$`)
		r3 = regexp.MustCompile(`^[-+]?\d+(\.\d+)?e[-+]?\d+$`)
	)

	if r1.MatchString(num) || r2.MatchString(num) || r3.MatchString(num) {
		return true
	}

	return false
}

func main() {
	input := []string{
		"123 ",
		" 0123",
		"-1.32",
		"+54",
		"10e2",
		"1.0e2",
		"1e-10",
	}

	for _, number := range input {
		fmt.Println(number, isNumber(number))
	}
}
