# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(cur):
            prev=None
            while cur:
                temp=cur.next
                cur.next=prev
                prev=cur
                cur=temp
            return prev
        l1=reverse(l1)
        l2=reverse(l2)
        carry=0
        dummy=ListNode(0)
        curr=dummy
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0 

            val=(v1+v2+carry)%10
            carry = 1 if v1+v2+carry>=10 else 0

            new_node=ListNode(val)
            curr.next=new_node
            curr=curr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        
        if carry:
            curr.next=ListNode(1)
        
        return reverse(dummy.next)