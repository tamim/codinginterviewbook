class MinStackOld:
    stk = []
    
    def __init__(self):
        self.stk = []
        
    def push(self, x):
        min_item = x
        if len(self.stk) > 0:
            top_item, min_item = self.stk[-1]
            
        if x < min_item:
            min_item = x
        
        self.stk.append((x, min_item))  

    def pop(self):
        if len(self.stk) > 0:
            self.stk.pop()
        
    def top(self):
        if len(self.stk) > 0:
            return self.stk[-1][0]
        else:
            raise Exception('Stack is empty')

    def getMin(self):
        if len(self.stk) == 0:
            raise Exception('Stack is empty')
        return self.stk[-1][1]


class MinStack:
    stk = []
    min_stk = []
    
    def __init__(self):
        self.stk = []
        self.min_stk = []
        
    def push(self, x):
        self.stk.append(x)
        if len(self.min_stk) == 0 or x < self.min_stk[-1]:
            self.min_stk.append(x) 

    def pop(self):
        if len(self.stk) == 0:
            raise Exception('Stack is empty')
        if self.min_stk[-1] == self.stk[-1]:
            self.min_stk.pop()
        self.stk.pop()
        
    def top(self):
        if len(self.stk) == 0:
            raise Exception('Stack is empty')
        return self.stk[-1]

    def getMin(self):
        if len(self.min_stk) == 0:
            raise Exception('Stack is empty')
        return self.min_stk[-1]
        

if __name__ == "__main__":
    min_stack = MinStack()

    min_stack.push(10)
    min_stack.push(6)
    min_stack.push(8)
    min_stack.push(9)
    min_stack.push(2)
    min_stack.push(5)

    assert 5 == min_stack.top()
    assert 2 == min_stack.getMin()
    
    min_stack.pop()

    assert 2 == min_stack.top()
    assert 2 == min_stack.getMin()

    min_stack.pop()

    assert 9 == min_stack.top()
    assert 6 == min_stack.getMin()

    min_stack.pop()

    assert 8 == min_stack.top()
    assert 6 == min_stack.getMin()

    min_stack.pop()

    assert 6 == min_stack.top()
    assert 6 == min_stack.getMin()

    min_stack.pop()

    assert 10 == min_stack.top()
    assert 10 == min_stack.getMin()

    min_stack.pop()

    assert -1 == min_stack.top()
    assert -1 == min_stack.getMin()
