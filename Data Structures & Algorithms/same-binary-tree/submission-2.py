# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # ## Recursive DFS -------
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if p is None and q is None:
    #         return True

    #     if p and q and p.val == q.val:
    #         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
    #     else:
    #         return False

    # ## Iterative DFS -------
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     stack = [(p,q)]

    #     while stack:
    #         n1,n2 = stack.pop()
    #         if n1 is None and n2 is None:
    #             continue
    #         if (n1 is None) or (n2 is None) or (n1.val != n2.val):
    #             return False

    #         stack.append((n1.left, n2.left))
    #         stack.append((n1.right, n2.right))

    #     return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((p,q))

        while queue:
            n1,n2 = queue.popleft()
            if n1 is None and n2 is None:
                continue
            if (n1 is None) or (n2 is None) or (n1.val != n2.val):
                return False

            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))

        return True




