class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        nums.sort()

        def dfs(i):
            print(f'i:{i-1}, subset:{subset}, res:{res}')
            if i >= len(nums):
                if subset not in res:
                    res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res