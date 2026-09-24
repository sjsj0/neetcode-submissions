class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        area=0

        f=True

        while l<r:
            temparea = min(heights[l], heights[r]) * abs(l-r)
            # print(temparea, l, r, heights[l], heights[r])
            area = max(area,temparea)

            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        
        return area

