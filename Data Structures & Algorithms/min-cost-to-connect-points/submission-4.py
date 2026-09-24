# class DSU:
#     def __init__(self,n):
#         self.Parent = list(range(n+1))
#         self.Size = [1]*(n+1)

#     def find(self, node):
#         if self.Parent[node] != node:
#             self.Parent[node] = self.find(self.Parent[node])
#         return self.Parent[node]

#     def union(self, u ,v):
#         pu = self.find(u)
#         pv = self.find(v)
#         if pu == pv:
#             return False        ## already u,v are part so no need to join it again, return False
        
#         if self.Size[pu] < self.Size[pv]:
#             pu,pv = pv,pu

#         self.Size[pu] += self.Size[pv]
#         self.Parent[pv] = pu
#         return True

## Kruskal's Algorithm -----------------------------------
# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         n = len(points)
#         edges = []
#         for i in range(n):
#             x1,y1 = points[i]
#             for j in range(i+1,n):
#                 x2,y2 = points[j]
#                 dist = abs(x1-x2) + abs(y1-y2)
#                 edges.append((dist, i,j))

#         edges.sort()
#         dsu = DSU(n)
#         res = 0
#         for dist, u, v in edges:
#             if dsu.union(u,v):
#                 res+=dist
            
#         return res

## Prim's Algorithm -------------------------------------
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)}
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]

                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])


        res = 0
        visit = set()
        minHeap = [[0,0]]
        while len(visit) < n:
            cost, nodeI = heapq.heappop(minHeap)
            if nodeI in visit:
                continue
            
            res += cost
            visit.add(nodeI)
            for neiCost, nei in adj[nodeI]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])
        
        return res





