class ListNode:
    def __init__(self, item):
        self.value = item
        self.next = None

def detect_cycle(head):
    if head.next is None:
        return None
    if head.next.next is None:
        return None
        
    slow, fast = head, head
    slow = slow.next
    fast = fast.next.next
    
    while slow != fast:
        slow = slow.next
        if slow is None:
            return None
        if fast.next is None:
            return None
        fast = fast.next.next
        if fast is None:
            return None
    
    node = head
    while node != slow:
        node = node.next
        slow = slow.next
        
    return node
