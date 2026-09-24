# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = deque()
        print(p.val)

        temp = root
        ## search
        while temp:
            print(temp.val)
            if temp.val == p.val:
                queue.append(temp)
                break
            elif p.val < temp.val:
                queue.append(temp)
                temp = temp.left
            else:
                queue.append(temp)
                temp = temp.right

        temp = root
        last = None

        # while queue:
        #     print(queue.popleft().val)

        while temp and queue:
            if temp.val == q.val:
                popped = queue.popleft()
                if temp == popped:
                    last = popped
                else:
                    return last
                
                break

            elif q.val < temp.val:
                popped = queue.popleft()
                if temp == popped:
                    last = popped
                else:
                    return last

                temp = temp.left
            else:
                popped = queue.popleft()
                if temp == popped:
                    last = popped
                else:
                    return last

                temp = temp.right
            
            print(last.val)
        
        return last