class ListNode:
   def __init__(self, item):
       self.value = item
       self.next = None

# Remove duplicates from sorted list
def remove_duplicates(head):
    node = head
    
    if node is None:
        return node
    
    while node:
        while node.next and node.val == node.next.val:
            node.next = node.next.next
        node = node.next
            
    return head

# Remove duplicates from sorted list - 2
def remove_duplicates(head):
    if head is None:
        return head
        
    head, prev = None, None
    current_old, current = None, head
    
    while current:
        current_old = current
        while current.next and current.val == current.next.val:
            current = current.next
        if current_old == current:
            if head is None:
                head = current_old
            else:
                prev.next = current_old
            current = current.next
            prev = current_old
            prev.next = None
        else:
            current = current.next       
                    
    return head
