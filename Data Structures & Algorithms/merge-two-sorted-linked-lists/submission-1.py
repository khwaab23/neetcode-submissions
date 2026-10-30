# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        dummy=ListNode(0)
        head1=dummy.next=list1 if list1.val<=list2.val else list2
        head2=list2 if dummy.next==list1 else list1
        while head1.next:
            if head1.next.val<=head2.val:
                head1=head1.next
            else:
                temp=head1.next
                head1.next=head2
                head1=temp
                head1,head2=head2,head1

        head1.next=head2

        return dummy.next