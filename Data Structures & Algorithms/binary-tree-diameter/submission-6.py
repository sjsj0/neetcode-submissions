# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # ## Brute Force BFS ------------------------
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return None

    #     q = deque()
    #     height=0
    #     q.append(root)

    #     while q:
    #         node = q.popleft()
    #         if node.left:
    #             q.append(node.left)
    #         if node.right:
    #             q.append(node.right)
                
    #         height = max(height, self.findRoot(node))

    #     return height
        
        
        
    # def findRoot(self, root:Optional[TreeNode]) -> int:
    #     if not root:
    #         return None

    #     lh = 0
    #     stack = []
    #     if root.left:
    #         stack.append((root.left, lh+1))

    #     while stack:
    #         node, height = stack.pop()
    #         if node.left:
    #             stack.append((node.left, height+1))
    #         if node.right:
    #             stack.append((node.right, height+1))
    #         lh = max(lh, height)
                        
    #     rh = 0
    #     stack = []
    #     if root.right:
    #         stack.append((root.right, rh+1))

    #     while stack:
    #         node, height = stack.pop()
    #         if node.left:
    #             stack.append((node.left, height+1))
    #         if node.right:
    #             stack.append((node.right, height+1))
    #         rh = max(rh, height)

    #     return lh+rh


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            leftHeight = self.maxHeight(root.left)
            rightHeight = self.maxHeight(root.right)
            diameter = leftHeight + rightHeight
            sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
            return max(diameter, sub)


    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1+ max(self.maxHeight(root.left), self.maxHeight(root.right))