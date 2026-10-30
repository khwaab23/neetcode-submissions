# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 
        q=deque()
        q.append((root,root.val))

        good=0
        while q:
            for _ in range(len(q)):
                node,pathmax=q.popleft()
                if pathmax<=node.val:
                    good+=1
                    pathmax=node.val
                
                if node.left:
                    q.append((node.left,pathmax))
                if node.right:
                    q.append((node.right,pathmax))
        
        return good
                