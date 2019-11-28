package main

import (
	"fmt"
	"strings"
)

func isRotation(s1, s2 string) bool {
	s := s1 + s1
	if len(s1) == len(s2) && strings.Contains(s, s2) {
		return true
	}
	return false
}

func main() {
	s1 := "Bangladesh"
	s2 := "Bangla"
	s3 := "Bangladesi"
	s4 := "deshBangla"

	fmt.Println(s1, s2, isRotation(s1, s2))
	fmt.Println(s1, s3, isRotation(s1, s3))
	fmt.Println(s1, s4, isRotation(s1, s4))
}
