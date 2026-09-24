class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # ans=[]
        # for i in range(len(nums)-k+1):
        #     # subList = nums[i:i+k]
        #     # ans.append(max(subList))
        #     ans.append(max(nums[i:i+k]))

        # return ans
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            print(f'queue:{q}, l:{l}, r:{r}')
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            if l > q[0]:
                q.popleft()
            r += 1
            print(f'------>queue:{q}, l:{l}, r:{r}')

        return output
