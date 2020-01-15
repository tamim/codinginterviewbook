
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def flatten(root):
    if root is None:
        return root
        
    li = []
    
    def preorder(node):
        if node is None:
            return
        li.append(node)
        preorder(node.left)
        preorder(node.right)
        
    preorder(root)
    
    li.append(None)
    
    for i, item in enumerate(li):
        if item is None:
            break
        item.left = None
        item.right = li[i+1]
        
    return li[0]
    
    
if __name__ == "__main__":
    # write test code here
