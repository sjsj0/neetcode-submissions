class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []

        closeMap = {"]":"[","}":"{",")":"("}

        for c in s:
            if c in closeMap:
                if my_stack and my_stack.pop() == closeMap[c]:
                    continue                    
                else:
                    return False
            
            else:
                my_stack.append(c)
                
        
        return True if not my_stack else False