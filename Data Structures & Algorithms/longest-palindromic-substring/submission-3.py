class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 1
        resIndex = 0
        n = len(s)

        for i in range(n):
            ## odd palindrome
            j=i-1
            k=i+1
            while j>=0 and k<n and s[j]==s[k]:
                if abs(k-j)+1>resLen:
                    resLen = abs(k-j)+1
                    resIndex = j
                j-=1
                k+=1
        


            ## even palindrome
            # if s[i]==s[i+1]:
            j=i
            k=i+1
            while j>=0 and k<n and s[j]==s[k]:
                if abs(k-j)+1>resLen:
                    resLen = abs(k-j)+1
                    resIndex = j
                j-=1
                k+=1
            

        return s[resIndex:resIndex+resLen]