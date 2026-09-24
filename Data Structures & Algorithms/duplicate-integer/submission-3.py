class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        z = set()
        for n in nums:
            if n in z:
                return True
            z.add(n)
        return False



        # if len(nums) == len((set(nums))):
        #     return False
        # return True