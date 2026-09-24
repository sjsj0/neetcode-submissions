class Solution:
    # ## Recursion -------------------------
    # def rob(self, nums: List[int]) -> int:
    #     n = len(nums)

    #     if n==1:
    #         return nums[0]
    #     if n==2:
    #         return max(nums)
    #     cache1 = [-1]*(n-1)
    #     cache2 = [-1]*(n-1)

    #     def dfs1(i):
    #         if i>=n-1:
    #             return 0

    #         if cache1[i]==-1:
    #             cache1[i] = max(nums1[i]+dfs1(i+2), dfs1(i+1))
    #         return cache1[i]

    #     def dfs2(i):
    #         if i>=n-1:
    #             return 0

    #         if cache2[i]==-1:
    #             cache2[i] = max(nums2[i]+dfs2(i+2), dfs2(i+1))
    #         return cache2[i]

    #     nums1 = nums[:n]
    #     nums2 = nums[1:]

    #     return max(dfs1(0), dfs2(0))

    # ## DP (Top-Down) ------------------------------
    # def rob(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     cache = [[-1]*2 for _ in range(n)]
    #     if n==1:
    #         return nums[0]

    #     def dfs(i, flag):
    #         if i>=n or (flag and i==n-1):
    #             return 0

    #         if cache[i][flag] == -1:
    #             cache[i][flag] = max(dfs(i+1, flag), nums[i]+dfs(i+2, flag))

    #         return cache[i][flag]

    #     return max(dfs(0,True), dfs(1,False))

    ## DP (Bottom-Up) -----------------------------
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))


    def helper(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        if n==1:
            return nums[0]

        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2,n):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])

        return dp[-1]


