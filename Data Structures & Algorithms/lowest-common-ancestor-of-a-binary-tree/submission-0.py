# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent={root:None}
        q1=deque([root])

        while p not in parent or q not in parent:
            node=q1.popleft()
            if node.left:
                parent[node.left]=node
                q1.append(node.left)
            if node.right:
                parent[node.right]=node
                q1.append(node.right)
        ancestors=set()   
        while p:
            ancestors.add(p)
            p=parent[p]
        
        while q not in ancestors:
            q=parent[q]
        return q

