class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # # Stack ---------------------
        # operators = '+-*/'
        # stack = []

        # for t in tokens:
        #     if t not in operators:
        #         stack.append(int(t))
        #     else:
        #         arg2 = stack.pop()
        #         arg1 = stack.pop()
        #         if t == "+":
        #             stack.append(arg1+arg2)
        #         elif t=="-":
        #             stack.append(arg1-arg2)
        #         elif t=="*":
        #             stack.append(arg1*arg2)
        #         elif t=="/":
        #             stack.append(int(arg1/arg2))
        #         else:
        #             print("Some other operator, not listed !!")
        #     print(stack)
        # return stack[0]

        # Recursion ---------------------
        def dfs():
            t = tokens.pop()
            if t in "+-*/":
                right = dfs()
                left = dfs()

                if t == "+":
                    return left + right
                elif t == "-":
                    return left - right
                elif t == "*":
                    return left * right
                elif t == "/":
                    return int(left / right)

            else:
                return int(t)
        
        ans = dfs()
        return ans            ## the func is getting called here
