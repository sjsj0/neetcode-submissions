# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ## Brute force ------------------------------------
        if not head:
            return

        curr = head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next

        i=0
        j=len(nodes)-1

        while i<j:
            nodes[i].next = nodes[j]
            i+=1

            if i>=j:
                break

            nodes[j].next = nodes[i]
            j-=1

        nodes[i].next = None ## clearing the next

        # ## Slow Fast technique ------------------------------------
        # slow = head
        # fast = head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # ## slow reaches to the centre of the linked list..
        # second = slow.next          ## starting point for the reverse list
        # slow.next = None            ## breaking the chain where slow stopped..

        # prev = None
        # while second:
        #     temp = second.next
        #     second.next = prev
        #     prev = second
        #     second = temp

        # first = head
        # second = prev

        # while second:
        #     temp1 = first.next
        #     temp2 = second.next

        #     first.next = second
        #     second.next = temp1

        #     first = temp1
        #     second = temp2