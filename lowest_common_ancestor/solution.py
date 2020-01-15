"""
এখানে লক্ষ করতে হবে যে, traverse() ফাংশনের ভেতরে আমি নোড খুঁজে পাওয়ামত্র return 1 করেছি, 
তাতে নোডটি পেয়ে গেলে আর নতুন নোড খোঁজা হবে না। 
"""

class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def find_lca(root, value1, value2):
    if not root:
        return -1
    
    def traverse(node, li, v):
        nonlocal ancestor
        if not node:
            return 0
        if node.value == v:
            ancestor = [x for x in li]
            return 1
        if node.left:
            return_value = traverse(node.left, li + [node.left.value], v)
            if return_value:
                return 1
        if node.right:
            return_value = traverse(node.right, li + [node.right.value], v)
            return return_value
        return 0
        
    ancestor = []
    a1 = []
    traverse(root, [root.value], value1)
    if ancestor == []:
        return -1
    a1 = [x for x in ancestor]
    
    ancestor = []
    a2 = []
    traverse(root, [root.value], value2)
    if ancestor == []:
        return -1
    a2 = [x for x in ancestor]
    
    lca = 0
    for x in zip(a1, a2):
        if x[0] == x[1]:
            lca = x[0]
            
    return lca
        
if __name__ == "__main__":
    # write test code here