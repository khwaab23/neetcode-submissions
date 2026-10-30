# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def balance(isBal,root):
            if not root:
                return [True,0]
            
            left=balance(isBal,root.left)
            right=balance(isBal,root.right)
            isBal= left[0] and right[0] and abs(left[1]-right[1])<=1
            return [isBal,1+max(left[1],right[1])]

        
        return balance(True,root)[0]