# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        q=deque()
        q.append((-float('inf'),root,float('inf')))
        while q:
            left,root,right=q.popleft()
            if not left<root.val<right:
                return False

            if root.left:
                q.append((left,root.left,root.val))
            
            if root.right:
                q.append((root.val,root.right,right))

        
        return True