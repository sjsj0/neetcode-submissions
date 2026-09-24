class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # my solution - some way of sliding window
        # temp = ""
        # maxLength=0
        # for c in s:
        #     while c in temp:
        #         temp = temp[1:]
            
        #     temp += c
            
        #     maxLength = max(maxLength, len(temp))

        # return maxLength

        # my solution - some way of sliding window
        hashMap = {}
        temp = ""
        maxLength=0
        for i, c in enumerate(s):
            if c in temp:
                index = hashMap[c]
                temp = s[index+1:i]
            
            temp += c
            hashMap[c] = i
            print(hashMap)
            maxLength = max(maxLength, len(temp))

        return maxLength