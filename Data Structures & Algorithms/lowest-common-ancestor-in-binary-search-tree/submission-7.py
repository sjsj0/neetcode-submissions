# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # ## Brute Force ------------------------
        # queue = deque()
        # print(p.val)

        # temp = root
        # ## search for p
        # while temp:
        #     print(temp.val)
        #     if temp.val == p.val:
        #         queue.append(temp)
        #         break
        #     elif p.val < temp.val:
        #         queue.append(temp)
        #         temp = temp.left
        #     else:
        #         queue.append(temp)
        #         temp = temp.right

        # temp = root
        # last = None

        # ## search for q, and calculating the lowest common ancestor
        # while queue:
        #     if temp.val == q.val:
        #         popped = queue.popleft()
        #         if temp == popped:
        #             last = popped
        #         else:
        #             return last
                
        #         break

        #     elif q.val < temp.val:
        #         popped = queue.popleft()
        #         if temp == popped:
        #             last = popped
        #         else:
        #             return last

        #         temp = temp.left
        #     else:
        #         popped = queue.popleft()
        #         if temp == popped:
        #             last = popped
        #         else:
        #             return last

        #         temp = temp.right
            
        #     print(last.val)
        
        # return last

        ## Single go -----------------------------
        temp = root
        # lastTemp = root

        while temp:
            if temp.val == p.val or temp.val == q.val:
                return temp

            pShift = 0
            qShift = 0

            pShift = -1 if p.val < temp.val else 1
            qShift = -1 if q.val < temp.val else 1

            print(f'pShift:{pShift}, qShift:{qShift}')

            if pShift == qShift:
                # lastTemp = temp
                temp = temp.left if pShift == -1 else temp.right

            else:
                return temp


            

