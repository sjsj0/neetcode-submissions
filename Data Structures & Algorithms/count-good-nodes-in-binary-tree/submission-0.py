# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        
        res = []

        def dfs(node, maximum):
            if not node:
                return
        
            if maximum <= node.val:
                res.append(node.val)
                maximum = max(maximum, node.val)
            
            dfs(node.left, maximum)
            dfs(node.right, maximum)

        dfs(root, root.val)

        print(res)

        return len(res)