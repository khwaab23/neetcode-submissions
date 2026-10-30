# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy=ListNode()
        dummy.next=head

        slow=head
        fast=head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        head1=head
        head2=slow.next
        slow.next=None
        prev=None
        curr=head2
        while curr:
            temp1=curr.next
            curr.next=prev
            prev=curr
            curr=temp1

        head2=prev

        while head2:
            temp1=head1.next
            temp2=head2.next

            head1.next=head2
            head2.next=temp1
            head1=temp1
            head2=temp2
        


        