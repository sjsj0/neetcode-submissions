class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []

        for c in s:
            if c in "([{":
                my_stack.append(c)
            else:
                if c == ")" and (len(my_stack)==0 or my_stack.pop() != "("):
                    return False
                if c == "]" and (len(my_stack)==0 or my_stack.pop() != "["):
                    return False
                if c == "}" and (len(my_stack)==0 or my_stack.pop() != "{"):
                    return False
        
        return len(my_stack) == 0