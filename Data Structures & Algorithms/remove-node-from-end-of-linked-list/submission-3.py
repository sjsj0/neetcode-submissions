# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        ## Brute force -----------------------------------------
        nodes = []
        temp = head

        while temp:
            nodes.append(temp)
            temp = temp.next

        removeIndex = len(nodes) - n
        if removeIndex == 0:
            return head.next

        nodes[removeIndex-1].next = nodes[removeIndex].next
        return head



        # ## Iteration (2 pass) -----------------------------------------
        # total=0
        # temp = head
        # while temp:
        #     total+=1
        #     temp = temp.next

        # removeIndex = total - n
        # if removeIndex == 0:
        #     return head.next

        # temp = head
        # i=0
        # while i<total:
        #     i+=1
        #     # starts chking from index no 1
        #     if i == removeIndex:
        #         temp.next = temp.next.next
        #         break

        #     temp = temp.next

        # return head
