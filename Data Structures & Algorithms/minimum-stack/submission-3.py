class MinStack:

    # brute force---------------
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

    # Two stacks-----------------
    # def __init__(self):
    #     self.stack = []
    #     self.minStack = []

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     newMinimum = min(val, self.minStack[-1] if self.minStack else val)
    #     self.minStack.append(newMinimum)

    # def pop(self) -> None:
    #     self.stack.pop()
    #     self.minStack.pop()
    
    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return self.minStack[-1]

    # One stack--------------------
    def __init__(self):
        self.stack = []
        self.min = float("inf")

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        # restoring old min
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]

        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min

