class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # l = 0
        # r = len(arr)

        # while l < r:
        #     mid = (l + r) // 2

        #     if arr[mid] < x:
        #         l = mid + 1
        #     else:
        #         r = mid

        # right = l
        # left = l - 1

        # for _ in range(k):

        #     if left < 0:
        #         right += 1

        #     elif right >= len(arr):
        #         left -= 1

        #     elif x - arr[left] <= arr[right] - x:
        #         left -= 1

        #     else:
        #         right += 1

        # return arr[left+1 : right]

# ---------------------------------------------------
        ## Think about two neighboring windows
        # arr[mid] vs arr[mid + k]
        left = 0
        right = len(arr) - k

        while left < right:

            mid = (left + right) // 2

            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]
