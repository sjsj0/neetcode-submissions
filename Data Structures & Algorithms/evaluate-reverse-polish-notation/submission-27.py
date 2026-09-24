class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = '+-*/'
        stack = []

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                arg2 = stack.pop()
                arg1 = stack.pop()
                if t == "+":
                    stack.append(arg1+arg2)
                elif t=="-":
                    stack.append(arg1-arg2)
                elif t=="*":
                    stack.append(arg1*arg2)
                elif t=="/":
                    stack.append(int(arg1/arg2))
                else:
                    print("Some other operator, not listed !!")
            print(stack)
        return stack[0]