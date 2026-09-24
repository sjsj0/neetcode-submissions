class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # # Binary search (2 pass) ----------------------
        # l=0
        # r=len(nums)-1

        # # find the minimum first, two get two sorted sub-arrays, and then do binary search on them..
        # while l<=r:
        #     mid = (l+r) // 2

        #     # sorted part
        #     if nums[mid] < nums[r]:
        #         r = mid
                    
        #     # unsorted part
        #     else:
        #         l = mid + 1

        # pivot = mid     ## mid is the minimum index
        # print(pivot)
        # l=0
        # r=len(nums)-1

        # ## checking target belongs to which sub-array..
        # if target >= nums[pivot] and target <= nums[r]:
        #     l = pivot
        # else:
        #     r = pivot - 1

        # ## doing binary search in that sub-array..
        # while l<=r:
        #     mid = (l+r) // 2

        #     if nums[mid] < target:
        #         l = mid + 1
        #     elif nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         return mid

        # return -1

        # Binary search (1 pass) ----------------------
        l=0
        r=len(nums)-1

        while l<=r:
            mid = (l+r) // 2

            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
