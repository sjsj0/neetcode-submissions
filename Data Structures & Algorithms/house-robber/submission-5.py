class Solution:
    # ## Recursion ------------------------------
    # def rob(self, nums: List[int]) -> int:
    #     n = len(nums)

    #     def dfs(i):
    #         if i>=n:
    #             return 0

    #         return max(nums[i]+dfs(i+2), dfs(i+1))

    #     return dfs(0)

    # ## DP (Top-Down) -------------------------------
    # def rob(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     cache = [-1]*n

    #     def dfs(i):
    #         if i>=n:
    #             return 0

    #         if cache[i] == -1:
    #             cache[i] = max(nums[i]+dfs(i+2), dfs(i+1))
    #         return cache[i]

    #     return dfs(0)


    ## DP (Bottom-Up) -------------------------------
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n==0:
            return 0
        elif n==1:
            return nums[0]
        
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])

        return dp[-1]

