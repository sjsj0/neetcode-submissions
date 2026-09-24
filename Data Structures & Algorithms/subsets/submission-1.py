class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def exclude(arr):
            if arr not in res:
                res.append(arr)
            if len(arr)>0:
                for i in range(len(arr)):
                    tempArr = arr[0:i] + arr[i+1:]
                    exclude(tempArr)

        exclude(nums)
        return list(res)