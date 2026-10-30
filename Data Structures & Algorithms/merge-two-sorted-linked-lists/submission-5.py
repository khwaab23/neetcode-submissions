# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1
        dummy=ListNode()
        l1,l2=list1,list2
        if l1.val>l2.val:
            l1,l2=l2,l1
        dummy.next=l1
        while l1.next :
            if l1.next.val >l2.val:
                temp=l1.next
                l1.next=l2
                l1=l2
                l2=temp
            else:
                l1=l1.next
            
        l1.next= l2

        return dummy.next



