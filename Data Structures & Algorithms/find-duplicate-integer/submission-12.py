class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            print(n)
            index = abs(n)-1
            if nums[index] < 1:
                return abs(n)
            else:
                nums[index] *= -1