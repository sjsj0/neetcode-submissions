class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans=0

        for i in range(n):
            leftMaximum = rightMaximum = height[i]

            for j in range(i):
                leftMaximum = max(leftMaximum, height[j])

            for j in range(i+1,n):
                rightMaximum = max(rightMaximum, height[j])
            
            ans += min(leftMaximum, rightMaximum) - height[i]

        return ans