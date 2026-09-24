class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ""
        maxLength=0
        for c in s:
            if c in temp:
                if temp[0] == c:
                    temp = temp[1:] + c
                
                else:
                    temp=""
                    temp += c
            else:
                temp += c
            
            maxLength = max(maxLength, len(temp))

        return maxLength