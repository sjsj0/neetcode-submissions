# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # ## Brute force -------------------------
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:

    #     if not root:
    #         return True
        
    #     leftHeight = self.findHeight(root.left)
    #     rightHeight  = self.findHeight(root.right)
    #     if abs(leftHeight - rightHeight) > 1:
    #         return False

    #     return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    # def findHeight(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0

    #     return 1 + max(self.findHeight(root.left), self.findHeight(root.right))

    ## DFS -------------------------
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:        
                return [True,0]

            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1
            return [balanced, 1+max(left[1],right[1])]

        return dfs(root)[0]