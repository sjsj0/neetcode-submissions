class Solution:

    # ## Two pointers --------------------------------
    # def longestPalindrome(self, s: str) -> str:
    #     resLen = 1
    #     resIndex = 0
    #     n = len(s)

    #     for i in range(n):
    #         ## odd palindrome
    #         j=i-1
    #         k=i+1
    #         while j>=0 and k<n and s[j]==s[k]:
    #             if abs(k-j)+1>resLen:
    #                 resLen = abs(k-j)+1
    #                 resIndex = j
    #             j-=1
    #             k+=1
        
    #         ## even palindrome
    #         # if s[i]==s[i+1]:
    #         j=i
    #         k=i+1
    #         while j>=0 and k<n and s[j]==s[k]:
    #             if abs(k-j)+1>resLen:
    #                 resLen = abs(k-j)+1
    #                 resIndex = j
    #             j-=1
    #             k+=1

    #     return s[resIndex:resIndex+resLen]

    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0
        n = len(s)

        dp = [[False]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i,n):
                if s[i]==s[j] and ((j-i+1<=2) or dp[i+1][j-1]):
                    dp[i][j]=True

                    if (j-i+1)>resLen:
                        resIdx=i
                        resLen=j-i+1

        return s[resIdx:resIdx+resLen]



