class TreeNode:
   def __init__(self, x):
       self.value = x
       self.left = None
       self.right = None

def path_sum(root, sum):
    result = []
    
    if root is None:
        return result
    
    def recurse(node, total, li):
        nonlocal result

        if total > sum: # if the tree has no negative nodes
            return
        
        if not node.left and not node.right:
            if total == sum:
                result.append([x for x in li])
                
        if node.left:
            li.append(node.left.value)
            recurse(node.left, total+node.left.value, li)
            li.pop()
            
        if node.right:
            li.append(node.right.value)
            recurse(node.right, total+node.right.value, li)
            li.pop()
            
    recurse(root, root.value, [root.value])
    return result

if __name__ == "__main__":
    # write your test code here          
    
