# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow=fast=head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        cur=slow.next
        slow.next=None
        prev=None
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        
        head1=head
        head2=prev
        MAXVAL=-float('inf')
        while head1:
            MAXVAL=max(head1.val+head2.val,MAXVAL)
            head1=head1.next
            head2=head2.next
        
        return MAXVAL