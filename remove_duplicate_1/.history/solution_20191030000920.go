package main

import "fmt"

type listNode struct {
	value int
	next  *listNode
}

func listNodeNew(val int) *listNode {
	var node *listNode = new(listNode)
	node.value = val
	node.next = nil
	return node
}

func main() {
	
}