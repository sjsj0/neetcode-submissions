class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)


        visited = set()
        components = 0

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for nei in adj[node]:
                dfs(nei)

        for n in range(n):
            print(n, visited)
            if n not in visited:
                components += 1
                dfs(n)
        
        return components
