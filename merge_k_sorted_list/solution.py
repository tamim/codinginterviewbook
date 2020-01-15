from heapq import heappush, heappop

class ListNode:
    def __init__(self, x):
        self.value = x    
        self.next = None


"""
linked_lists হচ্ছে লিঙ্কড লিস্টের লিস্ট (বা অ্যারে)। এটিতে প্রতিটি লিঙ্কড লিস্টের হেড নোড আছে।
"""
def merge_k_lists(linked_lists):
    h = [] # heap-এ আমরা (নোডের মান, নোড)-এভাবে টাপল রাখব। 
    for node in linked_lists:
        if node: # কোনো কোনো লিঙ্কড লিস্ট ফাঁকা থাকতে পারে, সেক্ষেত্রে node হবে None
            heappush(h, (node.value, node))
            
    head = ListNode(0)
    cur = head

    while len(h):
        # heappop() একটি টাপল রিটার্ন করবে যার প্রথম উপাদানটি হচ্ছে নোডের মান আর দ্বিতীয়টি হচ্ছে নোড
        # আমাদের দরকার কেবল নোড, তাই আমরা ইনডেক্স [1] ব্যবহার করছি
        cur.next = heappop(h)[1] 

        cur = cur.next 
                       
        if cur.next: # পরের নোড যদি থাকে, সেটিকে হিপে রাখতে হবে
            heappush(h, (cur.next.value, cur.next))
        
    return head.next

