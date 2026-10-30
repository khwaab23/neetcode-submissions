# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque()
        q.append((root,0))
        cols=defaultdict(list)
        mincol=maxcol=0
        while q: 
            # for _ in range
            node,col=q.popleft()
            cols[col].append(node.val)
            mincol=min(mincol,col)
            maxcol=max(maxcol,col)
            if node.left:
                q.append((node.left,col-1))
            if node.right:
                q.append((node.right,col+1))
        
        return [cols[c] for c in range(mincol,maxcol+1)]

