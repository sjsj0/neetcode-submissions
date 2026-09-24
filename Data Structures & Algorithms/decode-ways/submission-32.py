class Solution:

    # ## Recursion --------------------------
    # def numDecodings(self, s: str) -> int:
    #     n=len(s)
    #     res=0

    #     def dfs(i):
    #         nonlocal res
    #         if i>=n:
    #             print(i)
    #             res+=1
    #             return

    #         if s[i]=='0':
    #             return

    #         dfs(i+1)
    #         if i<n-1 and int(s[i:i+2])<=26:
    #             dfs(i+2)

    #     dfs(0)
    #     return res


    # ## DP (Top-Down) --------------------------
    # def numDecodings(self, s: str) -> int:
    #     n=len(s)
    #     cache = {}

    #     def dfs(i):
    #         if i>=n:
    #             print(i)
    #             return 1

    #         if s[i]=='0':
    #             return 0

    #         if i in cache:
    #             return cache[i]

    #         res = dfs(i+1)
    #         if i<n-1 and int(s[i:i+2])<=26:
    #             res += dfs(i+2)

    #         cache[i] = res
    #         return res

    #     return dfs(0)


    # ## DP (Bottom-Up) -----------------------------
    # def numDecodings(self, s: str) -> int:
    #     n=len(s)
    #     dp={n:1}
        
    #     for i in range(n-1, -1, -1):
    #         if s[i]=='0':
    #             dp[i]=0
    #         else:
    #             dp[i]=dp[i+1]

    #         if (i+1<n) and (s[i]=='1' or s[i]=='2' and s[i+1] in "0123456"):
    #             dp[i]+=dp[i+2]

    #     return dp[0]

    ## DP (Bottom-Up) - Space Optimized -----------------------------
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=dp2=0
        dp1=1
        
        for i in range(n-1, -1, -1):
            if s[i]=='0':
                dp=0
            else:
                dp=dp1

            if (i+1<n) and (s[i]=='1' or s[i]=='2' and s[i+1] in "0123456"):
                dp+=dp2
            
            dp,dp1,dp2 = 0,dp,dp1

        return dp1