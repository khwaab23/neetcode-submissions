class Solution: 
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        slow=fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        cur=slow.next 
        prev=None
        slow.next=None

        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp

        l1=head
        l2=prev

        while l1 and l2:
            temp1=l1.next
            temp2=l2.next
            l1.next=l2
            if temp1:
                l2.next=temp1
            l2=temp2
            l1=temp1
        
        return