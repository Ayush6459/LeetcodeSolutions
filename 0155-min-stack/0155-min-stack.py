class MinStack:

    def __init__(self):
        self.stack = list()
        self.minS = list()
        self.minElement = 2147483647

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minElement:
            self.minElement = val
        self.minS.append(self.minElement)

    def pop(self) -> None:
        self.stack.pop()
        self.minS.pop()
        if len(self.minS) != 0:
            self.minElement = self.minS[-1]
        else:
            self.minElement = 2147483647

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minS[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()