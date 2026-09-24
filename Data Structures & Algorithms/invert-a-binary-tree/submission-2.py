# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # ## BFS -------------------
        # q = deque()
        # q.append(root)

        # while q:
        #     t = q.popleft()
        #     if t:
        #         if t.left:
        #             q.append(t.left)
        #         if t.right:
        #             q.append(t.right)
        #         t.left,t.right = t.right, t.left

        # return root

        # ## Recursive DFS ----------------------
        # if not root:
        #     return None


        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root


        ## Iterative DFS ---------------------
        if not root:
            return None

        stack=[]
        stack.append(root)

        while stack:
            t = stack.pop()
            t.left, t.right = t.right, t.left

            if t.left:
                stack.append(t.left)
            if t.right:
                stack.append(t.right)

        return root
