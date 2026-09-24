class DSU:
    def __init__(self,n):
        self.Parent = [i for i in range(n+1)]
        self.Size = [1]*(n+1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        if self.Size[pu] < self.Size[pv]:
            pu,pv = pv,pu

        self.Parent[pv] = pu
        self.Size[pu] += self.Size[pv]
        return True

    def connected(self, u,v):
        return self.find(u)==self.find(v)



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

    # ## Binary Search + DFS -----------------------------------------
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


    #     l,r = minH, maxH
    #     while l<r:
    #         mid = (l+r)//2
    #         # m = (l + r) >> 1
    #         if dfs((0,0),mid):
    #             r=mid
    #         else:
    #             l=mid+1

    #         for row in range(n):
    #             for col in range(n):
    #                 visited[row][col]=False

    #     return r

    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        positions = sorted((grid[r][c], r,c) for r in range(n) for c in range(n))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        dsu = DSU(n*n)

        print(positions)
        for t,r,c in positions:
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if nr>=0 and nr<n and nc>=0 and nc<n and grid[nr][nc] <= t:
                    dsu.union(r*n+c, nr*n+nc)

            if dsu.connected(0, n*n-1):
                return t
