def generate_parenthesis(n):
    result = []
    
    def recurse(i, left, right, li):
        if i == 2 * n - 1:
            result.append("".join(li))
            return
        
        if left < n:
            li.append('(')
            recurse(i+1, left+1, right, li)
            li.pop()
        if right < left:
            li.append(')')
            recurse(i+1, left, right+1, li)
            li.pop()
            
    
    recurse(-1, 0, 0, [])
    
    return result

if __name__ == "__main__":
    for i in range(5):
        print(i, generate_parenthesis(i))
    
