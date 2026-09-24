# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # ## Recursive DFS ------------------
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     res = []
        
    #     def dfs(node):
    #         if not node:
    #             return
            
    #         dfs(node.left)
    #         res.append(node.val)
    #         dfs(node.right)

    #     dfs(root)

    #     return res[k-1]


    # ## Iterative DFS -----------------------
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     # res = [] ## extra, simply to print the nodes visited

    #     stack = []
    #     curr = root

    #     while stack or root:
    #         while curr:
    #             stack.append(curr)
    #             curr = curr.left
    #         curr = stack.pop()
    #         # res.append(curr.val) ## extra
    #         k-=1
    #         if k==0:
    #             return curr.val
    #         curr = curr.right


    ## Morris Traversal
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root

        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right

        return -1