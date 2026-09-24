# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    # ## Iteration --------------------------------------------------
    # def findMinIndex(self, lists: List[Optional[ListNode]]) -> int:
    #     minIndex = -1
    #     for i,node in enumerate(lists):
    #         if node is None:
    #             continue

    #         if minIndex == -1 or lists[minIndex].val > node.val:
    #             minIndex = i

    #     print(f'minIndex:{minIndex}')
    #     return minIndex

    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     dummy = temp = ListNode(-1)

    #     while True:
    #         print(temp.val)
    #         index = self.findMinIndex(lists)
    #         if index == -1:
    #             temp.next = None
    #             break
    #         temp.next = lists[index]
    #         lists[index] = lists[index].next
    #         temp = temp.next

    #     return dummy.next





    ## Iteration (one by one) -------------------------------
    def merge2Lists(self, l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next

            else:
                temp.next = l2
                l2 = l2.next
            
            temp = temp.next
        temp.next = l1 or l2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = temp = ListNode(float('-inf'))
        for node in lists:
            temp = self.merge2Lists(temp, node)

        return dummy.next




