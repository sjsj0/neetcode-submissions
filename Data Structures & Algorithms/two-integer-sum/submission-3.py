class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={value:index for index,value in enumerate(nums)}

        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in hashMap and hashMap[diff] != i:
                return [i,hashMap[diff]]