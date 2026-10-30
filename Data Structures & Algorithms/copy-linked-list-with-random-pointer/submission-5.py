"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        
        old_to_copy={None:None}

        cur=head
        while cur:
            new_node=Node(cur.val)
            old_to_copy[cur]=new_node
            cur=cur.next
        
        cur=head
        while cur:
            node=old_to_copy[cur]
            node.next=old_to_copy[cur.next]
            node.random=old_to_copy[cur.random]
            cur=cur.next
        
        return old_to_copy[head]
