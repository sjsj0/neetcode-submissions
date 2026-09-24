class Solution:

    # ## Backtracking ----------------------
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = []

    #     def backtrack(arr):
    #         if arr not in res:
    #             res.append(arr)
    #         if len(arr)>0:
    #             for i in range(len(arr)):
    #                 tempArr = arr[0:i] + arr[i+1:]
    #                 backtrack(tempArr)

    #     backtrack(nums)
    #     return list(res)

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

    ## Iteration --------------------------------
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = [[]]

    #     # for n in nums:
    #     #     res += [subset+[n] for subset in res]
    #     for n in nums:
    #         newSubset = []
    #         for subset in res:
    #             newSubset.append(subset+[n])
    #         print(f'n:{n}, res:{res}, --> newsubset:{newSubset}')
    #         res += newSubset
    #         print(f'res after merging:{res}')

    #     return res

    ## Bit manipulation ------------------------
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        for i in range(1<<n):       ## 2^n loops for each position of subset
            print(f'i:{i}')
            subset = []
            for j in range(n):
                if i & (1<<j):
                    subset.append(nums[j])
                    print(f'i:{i}, j:{j}, subset:{subset}')
            
            res.append(subset)

        return res