package main

import "fmt"

func isValid(A string) int {
	stack := make([]string, len(A), len(A))
	top := 0
	for i := range A {
		c := string(A[i])
		if c == "(" || c == "{" || c == "[" {
			stack[top] = c
			top++
		} else {
			if top < 1 {
				return 0
			}
			lastItem := stack[top-1]
			top--
			if (c == ")" && lastItem != "(") || (c == "}" && lastItem != "{") || (c == "]" && lastItem != "[") {
				return 0
			}
		}
	}

	if top == 0 {
		return 1
	}

	return 0
}

func main() {
	fmt.Println(isValid(""), 1)
	fmt.Println(isValid("()"), 1)
	fmt.Println(isValid("()()(){}[]"), 1)
	fmt.Println(isValid(")()()()"), 0)
	fmt.Println(isValid("()(){]"), 0)
	fmt.Println(isValid("((())"), 0)
}
