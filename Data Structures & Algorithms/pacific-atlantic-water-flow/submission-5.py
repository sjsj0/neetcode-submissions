class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        down = len(heights)
        right = len(heights[0])

        res = []

        def dfsPacific(r,c, currHt):
            if r<0 or r>=down or c<0 or c>=right or heights[r][c]==-1 or currHt<heights[r][c]:
                return False

            # print(r,c,currHt)
            ## Pacific
            if (r==0 or c==0):
                return True

            temp = heights[r][c]
            heights[r][c] = -1
            pa = dfsPacific(r-1,c, temp) or dfsPacific(r,c-1, temp) or dfsPacific(r+1,c, temp) or dfsPacific(r,c+1, temp)
            heights[r][c] = temp

            return pa

        def dfsAtlantic(r,c, currHt):
            if r<0 or r>=down or c<0 or c>=right or heights[r][c]==-1 or currHt<heights[r][c]:
                return False

            # print(r,c,currHt)
            ## Atlantic
            if (r==down-1 or c==right-1):
                return True

            temp = heights[r][c]
            heights[r][c] = -1
            pa = dfsAtlantic(r+1,c, temp) or  dfsAtlantic(r,c+1, temp)  or dfsAtlantic(r-1,c, temp) or dfsAtlantic(r,c-1, temp)
            heights[r][c] = temp

            return pa


        for r in range(down):
            for c in range(right):
                if dfsPacific(r,c, float('inf')) and dfsAtlantic(r,c, float('inf')):
                    res.append([r,c])


        return res

