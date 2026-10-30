# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr=dummy=ListNode(0)
        carry=0
        while l1 or l2 or carry:
            val1= l1.val if l1 else 0
            val2=l2.val if l2 else 0 
            digit_sum=(val1+val2+carry)%10
            carry=1 if val1+val2+carry>=10 else 0
            new_node=ListNode(digit_sum)
            curr.next=new_node
            curr=curr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        if carry:
            new_node=ListNode(1)
            curr.next=new_node
        return dummy.next


