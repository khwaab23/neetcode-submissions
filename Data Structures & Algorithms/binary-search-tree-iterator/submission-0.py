# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr=[-float('inf')]
        self.root=root
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            self.arr.append(root.val)
            inorder(root.right)
        inorder(self.root)
        self.itr=0
        

    def next(self) -> int:
        self.itr+=1
        return self.arr[self.itr]
        

    def hasNext(self) -> bool:
        return self.itr<len(self.arr)-1
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()