
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def invert_tree(node):
    if node is None:
        return node
        
    node.left, node.right = node.right, node.left
    invert_tree(node.left)
    invert_tree(node.right)
    
    return node

if __name__ == "__main__":
    # write your test code here