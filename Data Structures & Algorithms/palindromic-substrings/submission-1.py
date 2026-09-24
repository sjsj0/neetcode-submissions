class Solution:

    # ## DP (Bottom-Up) ----------------------------
    # def countSubstrings(self, s: str) -> int:
    #     res=0
    #     n=len(s)
    #     dp = [[False]*n for _ in range(n)]

    #     for i in range(n-1,-1,-1):
    #         for j in range(i,n):
    #             if s[i]==s[j] and ((j-i+1)<=2 or dp[i+1][j-1]):
    #                 dp[i][j]=True
    #                 res+=1

    #     return res

    ## Two pointers --------------------------------
    def countSubstrings(self, s: str) -> int:
        res=0
        n = len(s)

        for i in range(n):
            res+=1
            ## odd palindrome
            j=i-1
            k=i+1
            while j>=0 and k<n and s[j]==s[k]:
                res+=1
                j-=1
                k+=1
        
            ## even palindrome
            # if s[i]==s[i+1]:
            j=i
            k=i+1
            while j>=0 and k<n and s[j]==s[k]:
                res+=1
                j-=1
                k+=1

        return res