class Solution:

    ## BFS ---------------------------------
    def orangesRotting(self, grid: List[List[int]]) -> int:
        down = len(grid)
        right = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

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
                if 0<=row<down and 0<=col<right and grid[row][col] == 1 and (row,col,level+1) not in queue:
                    queue.append((row,col,level+1))

        print(grid)
        for r in range(down):
            for c in range(right):
                if grid[r][c] == 1:
                    return -1

        return level



