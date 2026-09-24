# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = [[root.val]]
        queue = deque()
        queue.append([root])

        while queue:
            tempArray = []
            tempNodes = []
            nodes = queue.popleft()

            for n in nodes:
                if n.left:
                    tempNodes.append(n.left)
                    tempArray.append(n.left.val)
                if n.right:
                    tempNodes.append(n.right)
                    tempArray.append(n.right.val)

            if tempNodes:
                queue.append(tempNodes)
                res.append(tempArray)
                print(res)

        return res