class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None


def find_max(root):
    max_v = root.data
    if root.left:
        left_max = find_max(root.left)
        if left_max > max_v:
            max_v = left_max
    if root.right:
        right_max = find_max(root.right)
        if right_max > max_v:
            max_v = right_max
    return max_v


def check_binary_search_tree(root):
    if root is None:
        return True
        
    # find the largest number on the left sub-tree and check if it's smaller/equal to the root
    if root.left:
        max_value = find_max(root.left)
        if max_value >= root.data:
            return False
    
    # find the smallest number on the right sub-tree and check if it's larger than the root
    if root.right:
        min_value = find_min(root.right)
        if min_value <= root.data:
            return False
    
    # now do the same for the sub-trees
    valid_left = check_binary_search_tree(root.left)
    valid_right = check_binary_search_tree(root.right)
        
    return valid_left and valid_right

def check_binary_search_tree_(root):
    nodes = []
    
    def inorder(root):
        if root is None:
            return
        inorder(root.left)    
        nodes.append(root.data)
        inorder(root.right)
            
    inorder(root)
    
    for i in range(len(nodes)-1):
        if nodes[i] >= nodes[i+1]:
            return False
        
    return True

def check_binary_search_tree(root):
    
    def inorder(root):
        nonlocal last_node
        
        if root is None: 
            return True
        
        left_valid = inorder(root.left)    
        if left_valid is False:
            return False
        
        if root.data <= last_node: 
            return False
        
        last_node = root.data
        
        return inorder(root.right)  
    
    last_node = -1 #assuming all nodes are non-negative
    return inorder(root)
