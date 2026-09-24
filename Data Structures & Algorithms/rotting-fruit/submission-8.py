class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # down = len(grid)
        # right = len(grid[0])

        # def dfs(r,c,value):
        #     if r<0 or r>=down or c<0 or c>= right or grid[r][c]==0:
        #         return

        #     if grid[r][c] > value or grid[r][c] == 1:
        #         grid[r][c] = value
        #     else:
        #         return

        #     dfs(r+1,c,value+1)
        #     dfs(r-1,c,value+1)
        #     dfs(r,c+1,value+1)
        #     dfs(r,c-1,value+1)

        # for r in range(down):
        #     for c in range(right):
        #         if grid[r][c] == 2:
        #             dfs(r+1,c,3)
        #             dfs(r-1,c,3)
        #             dfs(r,c+1,3)
        #             dfs(r,c-1,3)
        
        # print(grid)
        # ans = 0

        down = len(grid)
        right = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        hashMap = set()

        queue = deque()
        for r in range(down):
            for c in range(right):
                if grid[r][c] == 2:
                    queue.append((r,c,0))

        level = 0
        while queue:
            r,c, level = queue.popleft()
            print(r,c, level)
            grid[r][c] = 2
            for dr, dc in directions:
                row = r+dr
                col = c+dc
                if 0<=row<down and 0<=col<right and grid[row][col] == 1:
                    queue.append((row,col,level+1))

        print(grid)
        for r in range(down):
            for c in range(right):
                if grid[r][c] == 1:
                    return -1

        return level



