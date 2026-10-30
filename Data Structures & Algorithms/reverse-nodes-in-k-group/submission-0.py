# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        groupPrev=dummy

        while True:
            kth=self.getKth(groupPrev,k)
            if not kth:
                break
            prev=kth.next
            curr=groupPrev.next
            groupNext=kth.next
            while curr!=groupNext:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            temp=groupPrev.next
            groupPrev.next=kth
            groupPrev=temp
        return dummy.next

    def getKth(self,node,k):
        while node and k>0:
            k-=1
            node=node.next
        return node


