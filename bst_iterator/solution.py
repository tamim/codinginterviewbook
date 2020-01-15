

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    stk = []
    
    def __init__(self, root):
        node = root
        while node:
            self.stk.append(node)
            node = node.left

    def hasNext(self):
        return self.stk != []
        

    def next(self):
        next_val = self.stk[-1].val
        node = self.stk.pop()
        if node.right:
            node = node.right
            while node:
                self.stk.append(node)
                node = node.left
        return next_val
        
        
