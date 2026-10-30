# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def move(head):
            l=0
            while head:
                head=head.next
                l+=1
            return l
        
        l1=move(headA)
        l2=move(headB)
        print(l1,l2)
        curA,curB=headA,headB
        if l1<l2:
            l1,l2=l2,l1
            curA,curB=curB,curA
        
        while l1-l2:
            curA=curA.next
            l1-=1
        
        while curA:
            if curA==curB:
                return curA
            curA=curA.next
            curB=curB.next
        

