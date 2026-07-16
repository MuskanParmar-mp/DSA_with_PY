class mystack:
    def __init__(self):
        self.st = []  # stack ko list se banaya
    
    def insert(self, data):  # Push operation
        self.st.append(data)
    
    def delete(self):  # Pop operation
        if len(self.st) == 0:
            return "underflow"
        x = self.st[-1]  # top element
        self.st.pop()    # top element hatao
        return x
    
    def top(self):  # Peek - top element dikhao
        if len(self.st) == 0:
            return "stack is empty"
        return self.st[-1]  
    
    def size(self):
        return len(self.st)

m = mystack()
m.insert(20)
m.insert(120)
m.insert(22)
m.insert(21)
print("Top:", m.top())     
print("Size:", m.size())   