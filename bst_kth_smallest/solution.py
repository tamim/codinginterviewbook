
class TreeNode:
   def __init__(self, x):
       self.value = x
       self.left = None
       self.right = None


def kthsmallest(root, k):
    
    def inorder(node):
        nonlocal k
        if not node:
            return
        value = inorder(node.left)
        if value: 
            return value
        if k == 1: 
            return node.value
        k -= 1
        return inorder(node.right)
            
    return inorder(root)
