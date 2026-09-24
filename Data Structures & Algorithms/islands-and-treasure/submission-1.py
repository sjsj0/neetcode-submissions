class Solution:

    # ## DFS ---------------------------------------
    # def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    #     down = len(grid)
    #     right = len(grid[0])

    #     def dfs(r,c, value):
    #         print(r,c,value)
    #         if r<0 or r>= down or c<0 or c>= right or grid[r][c] == -1:
    #             return

    #         if grid[r][c] > value:
    #             grid[r][c] = value
    #         else:
    #             return

    #         dfs(r+1,c,value+1)
    #         dfs(r-1,c,value+1)
    #         dfs(r,c+1,value+1)
    #         dfs(r,c-1,value+1)

    #     for r in range(down):
    #         for c in range(right):
    #             if grid[r][c] == 0:
    #                 dfs(r+1,c,1)
    #                 dfs(r-1,c,1)
    #                 dfs(r,c+1,1)
    #                 dfs(r,c-1,1)

    ## BFS ---------------------------------------------
    ## BFS is perfect for shortest path in an unweighted grid.....
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        down = len(grid)
        right = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        INF = 2147483647

        queue = deque()
        for r in range(down):
            for c in range(right):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if 0 <= row < down and 0 <= col < right and grid[row][col] == INF:
                    grid[row][col] = grid[r][c] + 1
                    queue.append((row, col))
