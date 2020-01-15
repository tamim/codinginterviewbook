
class ListNode:
   def __init__(self, item):
       self.value = item
       self.next = None

def remove_nth_from_end(head, n):
    if n == 0:
        return head
        
    total = 0
    node = head
    while node:
        total += 1
        node = node.next
    
    if total < n:
        count = 1
    else:
        count = total - n + 1
    
    node = head
    prev = None
    while node:
        count -= 1
        if count == 0:
            if prev is None:
                return head.next
            prev.next = node.next
            return head
        prev = node
        node = node.next
