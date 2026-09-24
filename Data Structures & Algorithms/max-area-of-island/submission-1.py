class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        down = len(grid)
        right = len(grid[0])

        def dfs(r,c):
            if r<0 or r>=down or c<0 or c>= right or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            


        for r in range(down):
            for c in range(right):
                if grid[r][c] == 1:
                    newArea = dfs(r,c)
                    print(newArea)
                    res = max(res, newArea)

        return res