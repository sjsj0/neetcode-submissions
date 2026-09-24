class Solution:
    def trap(self, height: List[int]) -> int:
        
        # Brute Force
        # n = len(height)
        # ans=0

        # for i in range(n):
        #     leftMaximum = rightMaximum = height[i]

        #     for j in range(i):
        #         leftMaximum = max(leftMaximum, height[j])

        #     for j in range(i+1,n):
        #         rightMaximum = max(rightMaximum, height[j])
            
        #     ans += min(leftMaximum, rightMaximum) - height[i]

        # return ans

        # Prefix and Suffix array
        # n = len(height)
        # ans=0

        # leftMaximum = [0]*n
        # rightMaximum = [0]*n

        # leftMaximum[0] = height[0]
        # for i in range(1,n):
        #     leftMaximum[i] = max(leftMaximum[i-1], height[i])

        # rightMaximum[n-1] = height[n-1]
        # for i in range(n-2, -1, -1):
        #     rightMaximum[i] = max(rightMaximum[i+1], height[i])

        # for i in range(n):
        #     ans += min(leftMaximum[i], rightMaximum[i]) - height[i]

        # return ans

        # Two pointer
        l=0
        r=len(height)-1

        leftMax = height[l]
        rightMax = height[r]
        res = 0

        while l<r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]

            else:
                r-=1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res
