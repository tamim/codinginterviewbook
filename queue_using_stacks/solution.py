class MyQueue():
    def __init__(self):
        self.stk1 = []
        self.stk2 = []
    
    def peek(self):
        if len(self.stk2):
            return self.stk2[len(self.stk2)-1]
        return self.stk1[0]
        
        
    def pop(self):
        if len(self.stk2):
            return self.stk2.pop()
        
        for i in range(len(self.stk1)-1, -1, -1):
            self.stk2.append(self.stk1[i])
        self.stk1 = []
        
        return self.stk2.pop()
        
        
    def put(self, value):
        self.stk1.append(value)

if __name__ == "__main__":
    # এখানে কোড লিখে MyQueue ক্লাসের ব্যবহার দেখাতে হবে।