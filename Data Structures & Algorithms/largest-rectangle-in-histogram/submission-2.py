class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # # Brute Force
        # maxArea=0
        # for i,h in enumerate(heights):
        #     maxArea = max(maxArea,h)
        #     l=r=i
        #     while l>0 and heights[l-1]>=h:
        #         l-=1

        #     while r<len(heights)-1 and heights[r+1]>=h:
        #         r+=1

        #     maxArea = max(maxArea, h*(r-l+1))
        #     print(maxArea,h,l,r)

        # return maxArea

        # Two left and right stacks:
        n = len(heights)

        leftMost = [-1] * n
        rightMost = [n] * n

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                leftMost[i] = stack[-1]

            stack.append(i)
        print(leftMost)

        stack = []
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)
        print(rightMost)

        maxArea = 0
        for i in range(n):
            maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] - 1))
        
        return maxArea
            
