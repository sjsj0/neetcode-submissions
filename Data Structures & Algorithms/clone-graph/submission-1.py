"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    # ## DFS -----------------------------------------------
    # def __init__(self):
    #     self.hashMap = {}

    # def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    #     if node is None:
    #         return None
    #     if node in self.hashMap:
    #         return self.hashMap[node]

    #     copy = Node(node.val)
    #     self.hashMap[node] = copy

    #     temp = []
    #     for nei in node.neighbors:
    #         temp.append(self.cloneGraph(nei))

    #     copy.neighbors = temp
    #     return copy


    # ## DFS one way (almost same) -----------------------------------
    # def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    #     hashMap = {}

    #     def dfs(node):
    #         if node in hashMap:
    #             return hashMap[node]

    #         copy = Node(node.val)
    #         hashMap[node] = copy
    #         for nei in node.neighbors:
    #             copy.neighbors.append(dfs(nei))
    #         return copy

    #     return dfs(node) if node else None



    
    ## BFS ------------------------------------------------
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        hashMap = {}
        hashMap[node] = Node(node.val)

        queue = deque()
        queue.append(node)

        while queue:
            currNode = queue.popleft()
            temp = []
            for nei in currNode.neighbors:
                if nei not in hashMap:
                    hashMap[nei] = Node(nei.val)
                    queue.append(nei)
                
                temp.append(hashMap[nei])
                
            hashMap[currNode].neighbors = temp

        return hashMap[node]
