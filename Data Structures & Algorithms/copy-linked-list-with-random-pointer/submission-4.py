class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        start=dummy=Node(0)
        
        l1=head
        copy_list={None: None}
        while l1:
            new_node=Node(l1.val)
            copy_list[l1]=new_node
            dummy.next=new_node
            dummy=dummy.next
            l1=l1.next

        l2=head
        while l2:
            copy_list[l2].random=copy_list[l2.random]
            l2=l2.next

        
        return copy_list[head]