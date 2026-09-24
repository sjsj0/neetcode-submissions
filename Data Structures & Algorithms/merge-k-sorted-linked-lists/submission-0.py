# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def findMinIndex(self, lists: List[Optional[ListNode]]) -> int:
        minIndex = -1
        firstValue = True
        for i,node in enumerate(lists):
            if node is None:
                continue
            if firstValue:
                minIndex = i
                firstValue = False

            temp = min(lists[minIndex].val, node.val)
            if temp == node.val:
                minIndex = i

        print(f'minIndex:{minIndex}')
        return minIndex


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = temp = ListNode(-1)

        while True:
            print(temp.val)
            index = self.findMinIndex(lists)
            if index == -1:
                temp.next = None
                break
            temp.next = lists[index]
            lists[index] = lists[index].next
            temp = temp.next


        return dummy.next


