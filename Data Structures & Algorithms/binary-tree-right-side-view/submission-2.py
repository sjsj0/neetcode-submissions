# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # ## Recursive DFS -------------------------------
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     res = []
        
    #     def dfs(node, depth):
    #         if not node:
    #             return None

    #         if len(res) == depth:
    #             res.append([])
            
    #         res[depth].append(node.val)
    #         dfs(node.left, depth+1)
    #         dfs(node.right, depth+1)
        
    #     dfs(root,0)

    #     ans = []
    #     for r in res:
    #         ans.append(r[-1])
        
    #     return ans


    ## BFS -------------------------------
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])

        while queue:
            rightSide = None
            qLen = len(queue)

            for i in range(qLen):
                node = queue.popleft()
                if node:
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)
                
            if rightSide:
                res.append(rightSide.val)

        return res

