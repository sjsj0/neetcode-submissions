# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        ## Iteration (2 pass)
        total=0
        temp = head
        while temp:
            total+=1
            temp = temp.next

        removeIndex = total - n
        if removeIndex == 0:
            return head.next

        temp = head
        i=0
        while i<total:
            i+=1
            # starts chking from index no 1
            if i == removeIndex:
                temp.next = temp.next.next
                break

            temp = temp.next

        return head
