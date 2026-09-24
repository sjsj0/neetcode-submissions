# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # ## Recursive DFS --------------------------
    # def goodNodes(self, root: TreeNode) -> int:
    #     res = []
    #     def dfs(node, maximum):
    #         if not node:
    #             return
        
    #         if maximum <= node.val:
    #             res.append(node.val)
    #             maximum = max(maximum, node.val)
            
    #         dfs(node.left, maximum)
    #         dfs(node.right, maximum)

    #     dfs(root, root.val)
    #     print(res)
    #     return len(res)

    ## Recursive DFS --------------------------
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maximum):
            if not node:
                return 0
        
            res = 1 if maximum <= node.val else 0
            maximum = max(maximum, node.val)
            res += dfs(node.left, maximum)
            res += dfs(node.right, maximum)
            return res

        return dfs(root, root.val)

