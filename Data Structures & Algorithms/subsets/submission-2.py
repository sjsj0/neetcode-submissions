class Solution:

    ## Backtracking ----------------------
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(arr):
            if arr not in res:
                res.append(arr)
            if len(arr)>0:
                for i in range(len(arr)):
                    tempArr = arr[0:i] + arr[i+1:]
                    backtrack(tempArr)

        backtrack(nums)
        return list(res)

    # ## another way of Backtracking -------------------
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     subset = []

    #     def dfs(i):
    #         print(f'i:{i-1}, subset:{subset}, res:{res}')
    #         if i >= len(nums):
    #             res.append(subset.copy())
    #             return
    #         subset.append(nums[i])
    #         dfs(i + 1)
    #         subset.pop()
    #         dfs(i + 1)

    #     dfs(0)
    #     return res