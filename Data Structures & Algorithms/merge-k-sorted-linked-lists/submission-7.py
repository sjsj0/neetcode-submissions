# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    ## Iteration --------------------------------------------------
    def findMinIndex(self, lists: List[Optional[ListNode]]) -> int:
        minIndex = -1
        for i,node in enumerate(lists):
            if node is None:
                continue

            if minIndex == -1 or lists[minIndex].val > node.val:
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





    # # ## Iteration (one by one) -------------------------------
    # def merge2Lists(self, l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
    #     dummy = temp = ListNode()

    #     while l1 and l2:
    #         if l1.val <= l2.val:
    #             temp.next = l1
    #             l1 = l1.next

    #         else:
    #             temp.next = l2
    #             l2 = l2.next
            
    #         temp = temp.next
    #     temp.next = l1 or l2

    #     return dummy.next

    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     dummy = temp = ListNode(float('-inf'))
    #     for node in lists:
    #         temp = self.merge2Lists(temp, node)

    #     return dummy.next








    # ## Heap --------------------------------------------
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     minHeap = []

    #     for i,node in enumerate(lists):
    #         if node:
    #             heapq.heappush(minHeap, (node.val, i, node))

    #     dummy = temp = ListNode()

    #     while minHeap:
    #         val, i, node = heapq.heappop(minHeap)
    #         temp.next = node
    #         temp = temp.next

    #         if node.next:
    #             heapq.heappush(minHeap, (node.next.val, i, node.next))

    #     return dummy.next
    






    # ## Using Divide and Conquer ---------------------------------------------------------------------------------------
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     if not lists:
    #         return None

    #     def mergeRange(lists, left, right):
    #         if left == right:
    #             return lists[left]

    #         mid = (left + right) // 2
    #         l1 = mergeRange(lists, left, mid)
    #         l2 = mergeRange(lists, mid+1, right)

    #         return self.merge2Lists(l1,l2)

    #     return mergeRange(lists, 0, len(lists)-1)
