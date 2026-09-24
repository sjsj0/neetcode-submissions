class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # my solution - some way of sliding window(has error)
        temp = ""
        maxLength=0
        for c in s:
            while c in temp:
                temp = temp[1:]
            
            temp += c
            
            maxLength = max(maxLength, len(temp))

        return maxLength