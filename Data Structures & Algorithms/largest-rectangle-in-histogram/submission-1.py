class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        for i,h in enumerate(heights):
            maxArea = max(maxArea,h)
            l=r=i
            while l>0 and heights[l-1]>=h:
                l-=1

            while r<len(heights)-1 and heights[r+1]>=h:
                r+=1

            maxArea = max(maxArea, h*(r-l+1))
            print(maxArea,h,l,r)

        return maxArea