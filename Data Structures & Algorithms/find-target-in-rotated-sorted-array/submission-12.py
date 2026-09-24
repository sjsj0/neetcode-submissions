class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        # find the minimum first, two get two sorted sub-arrays, and then do binary search on them..
        while l<=r:
            mid = (l+r) // 2

            # sorted part
            if nums[mid] < nums[r]:
                r = mid
                    
            # unsorted part
            else:
                l = mid + 1

        pivot = mid
        print(pivot)
        l=0
        r=len(nums)-1

        ## checking target belongs to which sub-array..
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        ## doing binary search in that sub-array..
        while l<=r:
            mid = (l+r) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid


        return -1