# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res=-float('inf')
        def pathsum(root):
            if not root:
                return 0
            nonlocal res
            left=max(pathsum(root.left),0)
            right=max(pathsum(root.right),0)
            res=max(res,root.val+left+right)
            return root.val+max(left,right)
        pathsum(root)
        return res
