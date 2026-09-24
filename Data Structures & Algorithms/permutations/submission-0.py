class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        n = len(nums)
        def dfs(index, n):
            if index == n:
                res.append(nums.copy())
                return

            
            print(index, res)
            for i in range(index,n):
                nums[index], nums[i] = nums[i], nums[index]
                dfs(index+1,n)
                nums[i], nums[index] = nums[index], nums[i]

        dfs(0,n)
        
        return res




