class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]

        for src,dest,time in times:
            adj[src].append([dest,time])

        dist = {node: float('inf') for node in range(1, n+1)}

        def dfs(node, time):
            if time >= dist[node]:
                return

            dist[node] = time

            for nei, t in adj[node]:
                dfs(nei, time+t)



        dfs(k,0)
        res = max(dist.values())

        return res if res < float('inf') else -1