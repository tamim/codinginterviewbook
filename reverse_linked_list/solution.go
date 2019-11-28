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

func reverseListRecurse(node *listNode) *listNode {
	if node.next == nil {
		return node
	}
	nextNode := node.next
	head := reverseListRecurse(nextNode)
	node.next = nil
	nextNode.next = node

	return head
}

func reverseList(head *listNode) *listNode {
	nodeStack := []*listNode{}

	node := head

	for node != nil {
		nodeStack = append(nodeStack, node)
		node = node.next
	}

	for i := len(nodeStack) - 1; i > 0; i-- {
		nodeStack[i].next = nodeStack[i-1]
	}

	nodeStack[0].next = nil

	return nodeStack[len(nodeStack)-1]
}

func reverseList2(head *listNode) *listNode {
	prevNode := head
	node := head.next
	prevNode.next = nil
	for node != nil {
		//fmt.Println(prevNode.value, node.value)
		nextNode := node.next
		node.next = prevNode
		prevNode = node
		node = nextNode
	}

	head = prevNode

	return head
}

/*
start = node.next
current = start
prev = node
for _ in range(C-B+1):
	next_item = current.next
	current.next = prev
	prev = current
	current = next_item

start.next = current
node.next = prev
*/
func reverseListMN(head *listNode, m int, n int) *listNode {
	node := head
	var prev *listNode

	for i := 1; i < m; i++ {
		prev = node
		node = node.next
	}

	startNode := node
	prevNode := node
	node = node.next
	for i := m; i < n; i++ {
		nextNode := node.next
		node.next = prevNode
		prevNode = node
		node = nextNode
	}

	prev.next = prevNode
	startNode.next = node

	return head
}

func printList(head *listNode) {
	for head != nil {
		fmt.Println(head.value)
		head = head.next
	}
}

func main() {
	node1 := listNodeNew(1)
	node2 := listNodeNew(2)
	node3 := listNodeNew(3)
	node4 := listNodeNew(4)
	node5 := listNodeNew(5)

	head := node1
	node1.next = node2
	node2.next = node3
	node3.next = node4
	node4.next = node5

	//printList(head)

	// node := reverseList(head)
	// fmt.Println("")
	// printList(node)

	//head = reverseListRecurse(head)
	//printList(head)

	//head = reverseList2(head)

	head = reverseListMN(head, 2, 4)
	printList(head)
}
