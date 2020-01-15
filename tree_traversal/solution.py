class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

    def add_left_child(self, node):
        self.left = node

    def add_right_child(self, node):
        self.right = node


def inorder_traversal(node):
    if node.left:
        inorder_traversal(node.left)
    print(node.value)
    if node.right:
        inorder_traversal(node.right)


def inorder_traversal_using_stack(node):
    stk = []
    values = []
    
    while True:
        while node:
            stk.append(node)
            node = node.left
            
        if len(stk) == 0:
            break

        node = stk.pop()
        values.append(node.value)
        node = node.right
            
    return values

def postorder_traversal(node):
    if node.left:
        postorder_traversal(node.left)
    if node.right:
        postorder_traversal(node.right)
    print(node.value, end=" ")


"""
     1
    / \
   2   3
 /    / \
4    5   6
"""

if __name__ == "__main__":
    root = TreeNode(1)
    two, three, four, five, six = [TreeNode(x) for x in range(2, 7)]
    root.add_left_child(two)
    root.add_right_child(three)
    two.add_left_child(four)
    three.add_left_child(five)
    three.add_right_child(six)

    postorder_traversal(root)
    print()
    li = postorder_traversal_using_stack(root)
    print(li)



