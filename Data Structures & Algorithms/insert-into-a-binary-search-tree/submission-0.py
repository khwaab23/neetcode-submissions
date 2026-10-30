# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node=TreeNode(val)
        if not root:
            return new_node

        if root.val<new_node.val:
            root.right=self.insertIntoBST(root.right,val)

        else:
            root.left=self.insertIntoBST(root.left,val)
        
        return root