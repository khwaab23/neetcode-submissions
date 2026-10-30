# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=defaultdict(list)
        def dfs(root,count,height):
            if not root:
                return 
            
            dfs(root.left,count-1,height+1)
            res[count].append((height,root.val))
            dfs(root.right,count+1,height+1)
        
        dfs(root,0,0)
        final=[]
        for col in sorted(res):
            col_vals = sorted(res[col], key=lambda x: x[0])
            final.append([val for _, val in col_vals])
        
        return final
            

        

