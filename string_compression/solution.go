package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	input := "abbcccddddeeabbc"
	n := len(input)

	letters := make([]byte, 0, n)
	frequency := make([]int, 0, n)

	freq := 0
	for i := 0; i < n; i++ {
		freq++
		if i == n-1 || input[i] != input[i+1] {
			letters = append(letters, input[i])
			frequency = append(frequency, freq)
			freq = 0
		}
	}

	n = len(letters)
	output := make([]string, 0, n*2)
	for i := 0; i < n; i++ {
		output = append(output, string(letters[i]))
		output = append(output, strconv.Itoa(frequency[i]))
	}

	outputStr := strings.Join(output, "")

	fmt.Println(outputStr)

}
