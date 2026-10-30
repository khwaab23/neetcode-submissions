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
        count=0
        q=deque()
        pathmax=root.val
        q.append((root,pathmax))
        while q:
            for _ in range(len(q)):
                node,pathmax=q.popleft()
                if node.val>=pathmax:
                    pathmax=node.val
                    count+=1

                if node.left:
                    q.append((node.left,pathmax))
                if node.right:
                    q.append((node.right,pathmax))
        return count
                