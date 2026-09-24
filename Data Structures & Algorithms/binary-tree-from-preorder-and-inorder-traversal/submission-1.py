# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # ## DFS --------------------------------
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     if not preorder or not inorder:
    #         return None

    #     root = TreeNode(preorder[0])
    #     splitIndex = inorder.index(preorder[0])

    #     root.left = self.buildTree(preorder[1:splitIndex+1], inorder[:splitIndex])
    #     root.right = self.buildTree(preorder[splitIndex+1:], inorder[splitIndex+1:])

    #     return root

    ## DFS with HashMap -----------------------
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val:idx for idx,val in enumerate(inorder)}

        self.pre_idx = 0
        def dfs(l,r):
            if l>r:
                return None

            rootVal = preorder[self.pre_idx]
            root = TreeNode(rootVal)
            self.pre_idx += 1
            mid = indices[rootVal]

            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root

        return dfs(0, len(inorder)-1)
