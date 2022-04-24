class MinStack:

    def __init__(self):
        self.stack = []
        self.min_status = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_status or val <= self.min_status[-1]:
            self.min_status.append(val)

    def pop(self) -> None:
        if self.stack and self.stack.pop() == self.min_status[-1]:
            self.min_status.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_status[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()