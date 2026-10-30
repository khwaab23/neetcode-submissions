# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res=root.val

        def dfs(root):
            if not root:
                return 0
            
            nonlocal res

            left=dfs(root.left)
            right=dfs(root.right)

            left=max(0,left)
            right=max(0,right)
            res=max(res,root.val+left+right)

            return root.val+max(right,left)
        
        dfs(root)
        return res
            