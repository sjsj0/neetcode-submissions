# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = []
        stack.append(root)
        visited = {}

        tempRoot = None

        while stack:
            node = stack.pop()

            if node:
                if node.val == subRoot.val:
                    if self.sameTree(node,subRoot):
                        return True

                stack.append(node.left)
                stack.append(node.right)

        return False

    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack =[(p,q)]


        while stack:
            n1,n2 = stack.pop()

            if n1 is None and n2 is None:
                continue
            if n1 is None or n2 is None or n1.val != n2.val:
                return False

            stack.append((n1.left, n2.left))
            stack.append((n1.right, n2.right))

        return True
            