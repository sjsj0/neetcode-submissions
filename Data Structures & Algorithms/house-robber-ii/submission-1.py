class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n==1:
            return nums[0]
        if n==2:
            return max(nums)
        cache1 = [-1]*(n-1)
        cache2 = [-1]*(n-1)

        def dfs1(i):
            if i>=n-1:
                return 0

            if cache1[i]==-1:
                cache1[i] = max(nums1[i]+dfs1(i+2), dfs1(i+1))
            return cache1[i]

        def dfs2(i):
            if i>=n-1:
                return 0

            if cache2[i]==-1:
                cache2[i] = max(nums2[i]+dfs2(i+2), dfs2(i+1))
            return cache2[i]

        nums1 = nums[:n]
        nums2 = nums[1:]

        return max(dfs1(0), dfs2(0))