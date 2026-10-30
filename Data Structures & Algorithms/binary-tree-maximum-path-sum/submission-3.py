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
            leftm=dfs(root.left)
            rightm=dfs(root.right)
            left=max(0,leftm)
            right=max(0,rightm)

            res=max(res,root.val+left+right)

            return max(left,right)+root.val
        dfs(root)
        return res