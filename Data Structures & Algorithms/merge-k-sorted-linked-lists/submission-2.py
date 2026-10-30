# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        head=dummy=ListNode()
        dummy.next=lists[0]
    
            
        def merge(l1,l2):
            if l1.val>l2.val:
                l1,l2=l2,l1
            dummy=ListNode(0)
            dummy.next=l1
            while l1.next:

                if l1.next.val<=l2.val:
                    l1=l1.next
                else:
                    temp=l1.next
                    temp2=l2.next
                    l1.next=l2
                    l1=l2
                    l2=temp
            l1.next=l2 if l2 else None

            return dummy.next
        
        for i in range(1,len(lists)):
            dummy.next=merge(lists[i],dummy.next)

        return dummy.next



            

        

            