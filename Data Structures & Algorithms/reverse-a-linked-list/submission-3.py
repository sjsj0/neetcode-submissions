# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = None
        # if head is not None:
        #     temp = head.next
        #     head.next = prev
        #     prev = head
        # else:
        #     return None
        # while True:
        #     if temp is not None:
        #         head = temp
        #         temp = head.next
        #         head.next = prev
        #         prev = head
                

        #     else:
        #         return head

        # Iteration ----------------------
        # prev = None
        # curr = head

        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        
        # return prev

        # Recursion ----------------------
        if not head:
            return None

        newHead = head

        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head

        head.next = None



        return newHead