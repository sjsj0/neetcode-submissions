# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def add(self, l1: Optional[ListNode], l2: Optional[Listnode], carry: int) -> Optional[ListNode]:
        if not l1 and not l2 and carry == 0:
            return None

        val1 = val2 = 0
        if l1:
            val1 = l1.val
        if l2:
            val2 = l2.val

        total = val1 + val2 + carry

        if total >= 10:
            carry = total // 10
            total = total % 10
        else:
            carry = 0


        nextNode  = self.add(l1.next if l1 else None,
                            l2.next if l2 else None,
                            carry)

        return ListNode(total, nextNode)
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ## Recursion
        return self.add(l1,l2,0)

                
        # ## Iteration -----------------------------------------
        # temp = ListNode()
        # dummy = temp

        # carry = 0
        # val1 = val2 = 0
        # while l1 or l2 or carry:
        #     sum = 0
        #     sum += carry
        #     if l1 is not None:
        #         sum += l1.val
        #         l1 = l1.next

        #     if l2 is not None:
        #         sum += l2.val
        #         l2 = l2.next

        #     if sum >= 10:
        #         carry = sum // 10
        #         sum = sum % 10  
        #     else:
        #         carry = 0

        #     temp.next = ListNode(sum)
        #     temp = temp.next

        # return dummy.next
            
