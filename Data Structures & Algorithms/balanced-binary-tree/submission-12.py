# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    ## Brute Force random ---------------
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        print(f'root:{root.val}')

        leftHeight = rightHeight = 0

        leftHeight = self.findHeight(root.left)
        rightHeight  = self.findHeight(root.right)

        print(f'leftHeight:{leftHeight}, rightHeight:{rightHeight}')
        if not self.isBalanced(root.left):
            return False
        if not self.isBalanced(root.right):
            return False
        
        if abs(leftHeight - rightHeight) > 1:
            return False
        else:
            return True
        

    def findHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.findHeight(root.left), self.findHeight(root.right))

    # ## Brute force arranged -------------------------
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