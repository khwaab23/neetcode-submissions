# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        
        if not root:
            return False
        
        def subTree(root,subroot):
            if not root and not subroot:
                return True
            
            if root and subroot and subroot.val==root.val:
                return subTree(root.left,subroot.left) and subTree(root.right,subroot.right)

            return False
        
        if subTree(root,subRoot) or self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot):
            return True
        else:
            return False


