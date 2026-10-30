# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q=deque()
        q.append((root,root.val))
        good_nodes=0
        while q:
            node,pathmax=q.popleft()
            if node.val>=pathmax:
                pathmax=node.val
                good_nodes+=1
            
            if node.left:
                q.append((node.left,pathmax))
            
            if node.right:
                q.append((node.right,pathmax))
            
        return good_nodes
