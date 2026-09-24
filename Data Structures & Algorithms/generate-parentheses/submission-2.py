class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backT(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backT(openN+1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backT(openN, closedN+1)
                stack.pop()

        backT(0,0)
        return res
