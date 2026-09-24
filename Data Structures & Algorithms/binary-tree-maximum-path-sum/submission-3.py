# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        res = []

        def dfs(node):
            if not node.left and not node.right:
                res.append(node.val)
                return node.val

            if node.left:
                l1 = dfs(node.left)
            if node.right:
                l2 = dfs(node.right)

            if node.left and node.right:
                res.append(l1)
                res.append(l2)
                res.append(l1+node.val)
                res.append(l2+node.val)
                res.append(l1+l2+node.val)
                res.append(node.val)
                ans = max(l1+node.val, l2+node.val, node.val)
            elif node.left:
                res.append(l1)
                res.append(l1+node.val)
                res.append(node.val)
                ans = max(node.val, l1+node.val)
            else:
                res.append(l2)
                res.append(l2+node.val)
                res.append(node.val)
                ans = max(node.val, l2+node.val)

            print
            return ans

        dfs(root)

        return max(res)