# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res=0
        def diameter(root):
            nonlocal res
            if not root:
                return 0

            leftmax=diameter(root.left)
            rightmax=diameter(root.right)
            res=max(leftmax+rightmax,res)
            return 1+max(diameter(root.left),diameter(root.right))
        diameter(root)
        return res