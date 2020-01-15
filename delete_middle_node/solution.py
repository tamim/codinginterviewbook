class ListNode:
   def __init__(self, item):
       self.value = item
       self.next = None

def delete_middle_node(head):
    # যদি ফাঁকা লিঙ্কড লিস্ট থাকে অথবা
    # কেবল একটি নোড থাকে, তাহলে সেটি মুছে ফেললে লিঙ্কড লিস্টে আর কিছু থাকবে না
    # তাই None রিটার্ন করব।
    if head is None or head.next is None:
        return None

    prev, slow, fast = None, head, head

    while fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # slow হচ্ছে মাঝখানের নোড, এটি মুছে ফেলতে হবে
    prev.next = slow.next

    return head


def print_linked_list(node):
    while node:
        print(node.value)
        node = node.next


if __name__ == "__main__":
    n1, n2, n3, n4, n5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n5
    head = n1

    head = delete_middle_node(head)

    print_linked_list(head)