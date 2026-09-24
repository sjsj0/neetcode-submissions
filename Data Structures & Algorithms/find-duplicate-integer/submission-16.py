class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # ## Negative Marking ------------------------------
        # for i, n in enumerate(nums):
        #     print(n)
        #     index = abs(n)-1
        #     if nums[index] < 1:
        #         return abs(n)
        #     else:
        #         nums[index] *= -1

        # ## Binary search ---------------------------------
        # n = len(nums)
        # low = 1
        # high = n-1

        # while low < high:
        #     mid = (low+high) // 2

        #     compare = sum(1 for num in nums if num<=mid)

        #     if compare <= mid:
        #         low = mid + 1
        #     else:
        #         high = mid

        # return low

        # ## Bit manipulation ----------------------
        # n = len(nums)
        # res = 0
        # for b in range(32):
        #     x=y=0
        #     mask = 1<<b
        #     for num in nums:
        #         if num & mask:
        #             x += 1
            
        #     for num in range(1,n):
        #         if num & mask:
        #             y += 1
            
        #     if x>y:
        #         res |= mask

        # return res

        ## Fast and slow pointers ---------------------------
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(slow, fast)
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow