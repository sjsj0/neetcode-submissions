class Solution:

    # ## MaxHeap
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     nums = [-n for n in nums]
    #     heapq.heapify(nums)

    #     while k>1:
    #         heapq.heappop(nums)
    #         k-=1

    #     # return -nums[0]   ## or 
    #     return -heapq.heappop(nums)

    ## MinHeap
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        while len(nums)-k:
            heapq.heappop(nums)

        return heapq.heappop(nums)