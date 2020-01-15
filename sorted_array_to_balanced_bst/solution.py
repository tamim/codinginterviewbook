class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sorted_array_to_BST(A):
    if len(A) == 0:
        return None
        
    if len(A) == 1:
        return TreeNode(A[0])
        
    l = len(A)
    mid_indx = l // 2
    
    root = TreeNode(A[mid_indx])
    
    root.left = sorted_array_to_BST(A[:mid_indx])
    root.right = sorted_array_to_BST(A[mid_indx+1:])
        
    return root


if __name__ == "__main__":
    # write test code here