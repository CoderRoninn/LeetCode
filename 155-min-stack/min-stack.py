class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] # To keep min value in the stack

        

    def push(self, val: int) -> None: #O(1)
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        # Normally finding min value in the stack takes O(n)
        # But by means of min_stack method we can find with O(1)

    def pop(self) -> None: #O(1)
        if self.stack:
            top_value = self.stack.pop()
        if top_value == self.min_stack[-1]:
            self.min_stack.pop()   
        else:
            print("The stack is empty, so you do not implement this operation.")    
        

    def top(self) -> int: # O(1)
        if self.stack:
            return self.stack[-1]
        else:
            print("The stacj is empty, so you do not implement this operation.")    
        
        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            print("The stack is empty so, you do not implement this operation") 
    
    #Time complexity of this algorithm is O(1) because every function takes O(1)
    #Space complexity of this algorithm is O(n) where n is the number of elements in the stack          
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()