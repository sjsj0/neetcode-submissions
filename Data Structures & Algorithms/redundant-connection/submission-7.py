class Solution:
    # def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    #     adj = {i:[] for i in range(1,len(edges)+1)}
    #     for n1, n2 in edges:
    #         adj[n1].append(n2)
    #         adj[n2].append(n1)

    #     cycle = set()
    #     output = []

    #     def dfs(node, parentNode):
    #         if node in cycle:
    #             output.append([node,parentNode])
    #             return

    #         cycle.add(node)
    #         for nei in adj[node]:
    #             if nei == parentNode:
    #                 continue
    #             dfs(nei, node)
    #         cycle.remove(node)

    #     for i in range(1,len(edges)+1):
    #         dfs(i,-1)

    #     print(output)

    #     for e in edges[::-1]:
    #         if e in output:
    #             return e


    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]

        def dfs(node, parentNode):
            if node in cycle:
                return True

            cycle.add(node)
            for nei in adj[node]:
                if nei == parentNode:
                    continue
                if dfs(nei,node):
                    return True

            return False

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            cycle = set()


            if dfs(n1,-1):
                return [n1,n2]

        return []