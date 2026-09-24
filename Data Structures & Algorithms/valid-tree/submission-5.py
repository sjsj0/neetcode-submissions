class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adj = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        cycle = set()
        def dfs(node,parentNode):
            if node in cycle:
                return False
            
            cycle.add(node)
            for nei in adj[node]:
                if nei == parentNode:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True

        return dfs(0,-1) and len(cycle)==n