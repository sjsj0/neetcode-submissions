class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(1,len(edges)+1)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        cycle = set()
        output = []

        def dfs(node, parentNode):
            if node in cycle:
                output.append([node,parentNode])
                return

            cycle.add(node)
            for nei in adj[node]:
                if nei == parentNode:
                    continue
                dfs(nei, node)
            cycle.remove(node)

        for i in range(1,len(edges)+1):
            dfs(i,-1)

        print(output)

        for e in edges[::-1]:
            if e in output:
                return e