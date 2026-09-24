class MinStack:

    # brute force
    # def __init__(self):
    #     self.stack = []

    # def push(self, val: int) -> None:
    #     self.stack.append(val)

    # def pop(self) -> None:
    #     self.stack.pop()

    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return min(self.stack)

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
            self.stack.append(val)
            newMinimum = min(val, self.minStack[-1] if self.minStack else val)
            self.minStack.append(newMinimum)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
