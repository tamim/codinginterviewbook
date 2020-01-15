class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

def height(node):
    if node is None:
        return 0
        
    return max(height(node.left), height(node.right)) + 1

def is_balanced(node):
    if node is None:
        return 1
        
    left_balanced = is_balanced(node.left)
    right_balanced = is_balanced(node.right)
    left_height = height(node.left)
    right_height = height(node.right)
    
    return 1 if abs(left_height - right_height) <= 1 and left_balanced and right_balanced else 0
    
    
