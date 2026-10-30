# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        for i in range(1, len(lists)):
            lists[i] = self.merge(lists[i - 1], lists[i])

        return lists[-1]


    def merge(self,list1,list2):
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        head1=list1 if list1.val<=list2.val else list2
        head2=list2 if list1.val<=list2.val else list1

        dummy=ListNode(0)
        dummy.next=head1

        while head1.next:
            if head1.next.val<head2.val:
                head1=head1.next
            else:
                temp1=head1.next
                temp2=head2.next
                head1.next=head2
                head1=temp1
                head1,head2=head2,head1

        head1.next=head2
        return dummy.next
 
        
        
        

            