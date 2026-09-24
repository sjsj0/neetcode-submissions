"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def __init__(self):
        self.hashMap = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        if node in self.hashMap:
            return self.hashMap[node]

        copy = Node(node.val)
        self.hashMap[node] = copy

        temp = []
        for nei in node.neighbors:
            temp.append(self.cloneGraph(nei))

        copy.neighbors = temp

        return copy
