class Solution:
    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    #     down = len(heights)
    #     right = len(heights[0])

    #     res = []

    #     def dfsPacific(r,c, currHt):
    #         if r<0 or r>=down or c<0 or c>=right or heights[r][c]==-1 or currHt<heights[r][c]:
    #             return False

    #         # print(r,c,currHt)
    #         ## Pacific
    #         if (r==0 or c==0):
    #             return True

    #         temp = heights[r][c]
    #         heights[r][c] = -1
    #         pa = dfsPacific(r-1,c, temp) or dfsPacific(r,c-1, temp) or dfsPacific(r+1,c, temp) or dfsPacific(r,c+1, temp)
    #         heights[r][c] = temp

    #         return pa

    #     def dfsAtlantic(r,c, currHt):
    #         if r<0 or r>=down or c<0 or c>=right or heights[r][c]==-1 or currHt<heights[r][c]:
    #             return False

    #         # print(r,c,currHt)
    #         ## Atlantic
    #         if (r==down-1 or c==right-1):
    #             return True

    #         temp = heights[r][c]
    #         heights[r][c] = -1
    #         pa = dfsAtlantic(r+1,c, temp) or  dfsAtlantic(r,c+1, temp)  or dfsAtlantic(r-1,c, temp) or dfsAtlantic(r,c-1, temp)
    #         heights[r][c] = temp

    #         return pa


    #     for r in range(down):
    #         for c in range(right):
    #             if dfsPacific(r,c, float('inf')) and dfsAtlantic(r,c, float('inf')):
    #                 res.append([r,c])

    #     return res

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        down = len(heights)
        right = len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pacific = False
        atlantic = False
        res = []

        def dfs(r,c, currHt):
            nonlocal pacific, atlantic
            # if r<0 or r>=down or c<0 or c>=right or heights[r][c]==-1 or currHt < heights[r][c]:
            #     return

            if (r<0 or c<0):
                pacific = True
                return

            if (r >= down or c >= right):
                atlantic = True
                return

            if currHt < heights[r][c]:
                return

            temp = heights[r][c]
            heights[r][c] = float('inf')

            for dx, dy in directions:
                dfs(r + dx, c + dy, temp)
                if pacific and atlantic:
                    break
            heights[r][c] = temp

        for r in range(down):
            for c in range(right):
                pacific = False
                atlantic = False
                dfs(r,c, float('inf'))
                if pacific and atlantic:
                    res.append([r,c])


        return res
