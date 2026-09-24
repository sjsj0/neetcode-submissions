# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        dummy = temp

        carry = 0
        val1 = val2 = 0
        while l1 or l2 or carry:
            sum = 0
            sum += carry
            if l1 is not None:
                sum += l1.val
                l1 = l1.next

            if l2 is not None:
                sum += l2.val
                l2 = l2.next

            if sum >= 10:
                carry = sum // 10
                sum = sum % 10  
            else:
                carry = 0

            temp.next = ListNode(sum)
            temp = temp.next

        return dummy.next
            
