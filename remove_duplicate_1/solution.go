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

func printList(head *listNode) {
	for head != nil {
		fmt.Println(head.value)
		head = head.next
	}
}

func removeDuplicates(head *listNode) *listNode {
	counter := make(map[int]int)

	node := head
	previousNode := head
	previousNode.next = nil
	counter[node.value] = 1
	for node.next != nil {
		node = node.next
		if _, ok := counter[node.value]; ok {
			node = node.next
			if node == nil {
				break
			}
		}
		counter[node.value] = 1
		previousNode.next = node
		previousNode = node
	}

	return head
}

func removeDuplicates2(head *listNode) *listNode {
	currentNode := head

	for currentNode != nil {
		node := currentNode
		for node.next != nil {
			if node.next.value == currentNode.value {
				node.next = node.next.next
			} else {
				node = node.next
			}
		}
		currentNode = currentNode.next
	}

	return head
}

func main() {
	node1 := listNodeNew(1)
	node2 := listNodeNew(2)
	node3 := listNodeNew(1)
	node4 := listNodeNew(4)
	node5 := listNodeNew(2)

	head := node1
	node1.next = node2
	node2.next = node3
	node3.next = node4
	node4.next = node5

	head = removeDuplicates2(head)

	printList(head)
}
