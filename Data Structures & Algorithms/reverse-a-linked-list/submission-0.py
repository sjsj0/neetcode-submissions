# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        if head is not None:
            temp = head.next
            head.next = prev
            prev = head
        else:
            return None
        while True:
            if temp is not None:
                head = temp
                temp = head.next
                head.next = prev
                prev = head
                

            else:
                return head
