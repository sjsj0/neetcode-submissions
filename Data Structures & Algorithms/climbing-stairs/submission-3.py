class Solution:
    # def climbStairs(self, n: int) -> int:
    #     dp = [0]*(n+1)
    #     dp[0] = dp[1] = 1
    #     for i in range(2,n+1):
    #         dp[i] = dp[i-1]+dp[i-2]

    #     return dp[-1]


    # ## Recursion --------------------------
    # def climbStairs(self, n: int) -> int:
    #     def dfs(i):
    #         if i>=n:
    #             return i==n     ## i.e., True means 1
    #         return dfs(i+1)+dfs(i+2)

    #     return dfs(0)

    ## Recursion --------------------------
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n

        def dfs(i):
            if i>=n:
                return i==n     ## i.e., True means 1

            ## means i earlier cal for this value..            
            if cache[i] != -1:
                return cache[i]

            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]

        return dfs(0)

        return dfs(0)