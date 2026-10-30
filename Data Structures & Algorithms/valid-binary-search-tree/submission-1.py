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
            for _ in range(len(q)):
                left,node,right=q.popleft()
                
                if not (left<node.val<right):
                    return False
                
                if node.left:
                    q.append((left,node.left,node.val))
                if node.right:
                    q.append((node.val,node.right,right))
        

        return True
