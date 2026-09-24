# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # ## DFS ----------------------
        # if not root:
        #     return 0
        
        # stack = []
        # depth = 1
        # stack.append((root,depth))

        # while stack:
        #     node,d = stack.pop()
        #     if node.left:
        #         stack.append((node.left,d+1))
        #     if node.right:
        #         stack.append((node.right,d+1))

        #     depth = max(depth,d)

        # return depth



        ## BFS ----------------------
        if not root:
            return 0
        
        q = deque()
        depth = 1
        q.append((root,depth))

        while q:
            node,d = q.popleft()
            if node.left:
                q.append((node.left,d+1))
            if node.right:
                q.append((node.right,d+1))

            depth = max(depth,d)

        return depth

