class ListNode:
   def __init__(self, item):
       self.value = item
       self.next = None

# স্ট্যাক ব্যবহার করে সমাধান
def is_palindrome(head):
    stk = []
    
    node = head
    
    while node:
        stk.append(node.val)
        node = node.next
        
    node = head
    while node:
        if node.val != stk[-1]:
            return False
        node = node.next
        stk.pop()
        
    return True
"""
    def lPalin(self, A):
        count = 0
        node = A
        while node:
            count += 1
            node = node.next
        prev = None
        curr = A
        for i in range(count // 2):
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        if count % 2 == 1:
            curr = curr.next
        while curr:
            if curr.val != prev.val:
                return 0
            curr = curr.next
            prev = prev.next
        return 1
       


"""
def is_palindrome(head):
    count = 0
    node = head
    while node:
        count += 1
        node = node.next

    # এখন লিঙ্কড লিস্টের প্রথম অর্ধেক অংশ উল্টে দিই
    prev, node = None, head
    for _ in range(count/2):
        temp_node, node.next = node.next, prev
        prev, node = node, temp_node

    # বেজোড় সংখ্যক নোড থাকলে মাঝখানের নোডটি কারো সঙ্গে তুলনা করা হবে না
    # তাই পরবর্তি নোডে চলে যেতে হবে, কারণ সেখান থেকে তুলনা করা শুরু হবে।
    if count % 2 == 1:
        node = node.next

    while node:
        if node.value != prev.value:
            return False
        node, prev = node.next, prev.next

    return True

    
