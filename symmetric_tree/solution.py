class TreeNode:
   def __init__(self, x):
       self.value = x
       self.left = None
       self.right = None


def is_symmetric1(root):
    if root is None:
        return 1
        
    left = []
    right = []
    
    def traverse1(node):
        if node is None:
            return
        left.append(node.value)
        traverse1(node.left)
        traverse1(node.right)
        
    def traverse2(node):
        if node is None:
            return
        right.append(node.value)
        traverse2(node.right)
        traverse2(node.left)
        
    traverse1(A.left)
    traverse2(A.right)
    
    return left == right
        

def is_symmetric2(root):
    if root is None:
        return True

    def _is_symmetric(lt, rt):
        if lt is None and rt is None:
            return True
        if lt is None or rt is None:
            return False

        if lt.value == rt.value:
            return _is_symmetric(lt.left, rt.right) and _is_symmetric(lt.right, rt.left)
        
        return False


    return _is_symmetric(root.left, root.right)


if __name__ == "__main__":
    # write code to test the functions