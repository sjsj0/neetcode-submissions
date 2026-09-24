class DoublyLinkedList:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

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

        # # Recursion ---------------------
        # def dfs():
        #     t = tokens.pop()
        #     if t in "+-*/":
        #         right = dfs()   # generally this stops at one level after getting a no
        #         left = dfs()    # this grows

        #         if t == "+":
        #             return left + right
        #         elif t == "-":
        #             return left - right
        #         elif t == "*":
        #             return left * right
        #         elif t == "/":
        #             return int(left / right)

        #     else:
        #         return int(t)
        
        # ans = dfs()     ## the func is getting called here
        # return ans

        # Doubly Linked List
        head = DoublyLinkedList(tokens[0])
        curr = head

        for t in tokens[1:]:
            curr.next = DoublyLinkedList(t, prev=curr)
            curr = curr.next

        while head is not None:
            if head.val in "+-*/":
                l = int(head.prev.prev.val)
                r = int(head.prev.val)

                if head.val == "+":
                    res = l + r
                elif head.val == "-":
                    res = int(l - r)
                elif head.val == "*":
                    res = int(l * r)
                elif head.val == "/":
                    res = int(l / r)

                head.val = str(res)
                head.prev = head.prev.prev.prev             ## last 2 were taken care of
                if head.prev is not None:
                    head.prev.next = head
            
            ans = int(head.val)
            head = head.next


        return ans
