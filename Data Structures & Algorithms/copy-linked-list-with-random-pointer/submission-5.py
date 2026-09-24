"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def __init__(self):
        self.hashMap = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        ## Recursion -----------------------------------------
        if head is None:
            return None
        if head in self.hashMap:
            return self.hashMap[head]           ##returns the address of the new copy  

        copy = Node(head.val)
        self.hashMap[head] = copy
        copy.next = self.copyRandomList(head.next)
        copy.random = self.hashMap.get(head.random)

        return copy

        # ## HashMap (2 pass) -----------------------------------------
        # hashMap = {None: None}

        # cur = head
        # while cur:
        #     copy = Node(cur.val)
        #     hashMap[cur] = copy
        #     cur = cur.next

        
        # cur = head
        # while cur:
        #     copy = hashMap[cur]
        #     copy.next = hashMap[cur.next]
        #     copy.random = hashMap[cur.random]
        #     cur = cur.next

        # return hashMap[head]


        # ## HashMap (1 pass) -----------------------------------------
        # hashMap = defaultdict(lambda: Node(0))
        # hashMap[None] = None

        # cur = head
        # while cur:
        #     hashMap[cur].val = cur.val
        #     hashMap[cur].next = hashMap[cur.next]
        #     hashMap[cur].random = hashMap[cur.random]
        #     cur = cur.next
    
        # return hashMap[head]

