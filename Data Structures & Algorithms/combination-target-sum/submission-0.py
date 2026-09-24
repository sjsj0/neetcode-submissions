class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, temp, total):
            if total == target:
                res.append(temp.copy())
                return
            if i>=len(nums) or total > target:
                return
            
            temp.append(nums[i])
            dfs(i, temp, total+nums[i])
            temp.pop()
            dfs(i+1, temp, total)

        dfs(0, [], 0)

        return res