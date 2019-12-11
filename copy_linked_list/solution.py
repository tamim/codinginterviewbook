class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

def copy_list1(head):
        if head == None:
            return head

        new_head = Node(head.val)
        old_to_new = dict()
        old_to_new[head] = new_head

        node = head
        while node.next:
            node = node.next
            new_node = Node(node.val)
            old_to_new[node] = new_node

        node = head
        while node:
            new_node = old_to_new[node]
            new_node.next = old_to_new[node.next] if node.next else None
            new_node.random = old_to_new[node.random] if node.random else None
            node = node.next

        return new_head

def copy_list2(head):
    if head == None:
        return head

    new_head = Node(head.val)
    old_to_new = dict()
    old_to_new[head] = new_head

    node = head
    while node.next:
        node = node.next
        new_node = Node(node.val)
        old_to_new[node] = new_node

    for node, new_node in old_to_new.items():
        new_node.next = old_to_new[node.next] if node.next else None
        new_node.random = old_to_new[node.random] if node.random else None

    return new_head

