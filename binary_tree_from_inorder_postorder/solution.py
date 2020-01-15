class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def build_tree1(Inorder, Postorder):
    if len(Inorder) == 0:
        return None
        
    if len(Inorder) == 1:
        return TreeNode(Inorder[0])
        
    root = TreeNode(Postorder[-1])
    indx = Inorder.index(Postorder[-1])
    root.left = build_tree1(Inorder[:indx], Postorder[:indx])
    root.right = build_tree1(Inorder[indx+1:], Postorder[indx:-1])
        
    return root

# without recursion
def build_tree2(Inorder, Postorder):
    if len(Inorder) == 0:
        return None
        
    if len(Inorder) == 1:
        return TreeNode(Inorder[0])
        
    stk = []
    root = TreeNode(Postorder.pop())
    
    stk.append(root)

    while True:
        if Inorder[-1] != stk[-1].value:
            node = TreeNode(Postorder.pop())
            stk[-1].right = node
            stk.append(node)
        else:
            node = stk.pop()
            Inorder.pop()

            if len(Inorder) == 0:
                break

            if stk and Inorder[-1] == stk[-1].value:
                continue
            
            node.left = TreeNode(Postorder.pop())

            stk.append(node.left)
        
    return root
                
if __name__ == "__main__":
    # write your test code here