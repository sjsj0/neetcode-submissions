class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        down = len(grid)
        right = len(grid[0])

        def dfs(r,c, value):
            print(r,c,value)
            if r<0 or r>= down or c<0 or c>= right or grid[r][c] == -1:
                return

            if grid[r][c] > value:
                grid[r][c] = value
            else:
                return


            dfs(r+1,c,value+1)
            dfs(r-1,c,value+1)
            dfs(r,c+1,value+1)
            dfs(r,c-1,value+1)

        for r in range(down):
            for c in range(right):
                if grid[r][c] == 0:
                    dfs(r+1,c,1)
                    dfs(r-1,c,1)
                    dfs(r,c+1,1)
                    dfs(r,c-1,1)