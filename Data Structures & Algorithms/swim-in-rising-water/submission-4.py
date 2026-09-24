class Solution:
    # def swimInWater(self, grid: List[List[int]]) -> int:
    #     n = len(grid)
    #     visited = [[False] * n for _ in range(n)]

    #     def dfs(node, time):
    #         r,c = node
    #         if r<0 or c<0 or r>=n or c>=n or visited[r][c]:
    #             return float('inf')

    #         if r==n-1 and c==n-1:
    #             return max(time, grid[r][c])

    #         visited[r][c] = True
    #         time = max(time,grid[r][c])
    #         res = min(dfs((r+1,c),time),dfs((r-1,c),time),dfs((r,c+1),time),dfs((r,c-1),time))
    #         visited[r][c] = False
    #         return res

    #     return dfs((0,0),0)

    # ## DFS -----------------------------------------
    # def swimInWater(self, grid: List[List[int]]) -> int:
    #     n = len(grid)
    #     visited = [[False]*n for _ in range(n)]

    #     minH = maxH = grid[0][0]
    #     for row in range(n):
    #         maxH = max(maxH, max(grid[row]))
    #         minH = min(minH, min(grid[row]))

    #     def dfs(node, t):
    #         r,c = node
    #         if r<0 or c<0 or r>=n or c>=n or visited[r][c] or grid[r][c]>t:
    #             return False

    #         if r==(n-1) and c==(n-1):
    #             return True

    #         visited[r][c] = True
    #         return (dfs((r+1,c),t) or dfs((r-1,c),t) or dfs((r,c+1),t) or dfs((r,c-1),t))


    #     for t in range(minH, maxH):
    #         if dfs((0,0),t):
    #             return t
    #         for r in range(n):
    #             for c in range(n):
    #                 visited[r][c]=False


    #     return maxH

    ## Binary Search + DFS -----------------------------------------
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False]*n for _ in range(n)]

        minH = maxH = grid[0][0]
        for row in range(n):
            maxH = max(maxH, max(grid[row]))
            minH = min(minH, min(grid[row]))

        def dfs(node, t):
            r,c = node
            if r<0 or c<0 or r>=n or c>=n or visited[r][c] or grid[r][c]>t:
                return False

            if r==(n-1) and c==(n-1):
                return True

            visited[r][c] = True
            return (dfs((r+1,c),t) or dfs((r-1,c),t) or dfs((r,c+1),t) or dfs((r,c-1),t))


        l,r = minH, maxH
        while l<r:
            mid = (l+r)//2
            if dfs((0,0),mid):
                r=mid
            else:
                l=mid+1

            for row in range(n):
                for col in range(n):
                    visited[row][col]=False

        return r