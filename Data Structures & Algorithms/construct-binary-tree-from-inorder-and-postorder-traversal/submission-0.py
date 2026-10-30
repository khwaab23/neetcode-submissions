# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # if not inorder or not postorder:
        #     return None

        # root=TreeNode(postorder[-1])
        # idx=inorder.index(postorder[-1])
        # root.right=self.buildTree(inorder[idx+1:],postorder[idx:-1])
        # root.left=self.buildTree(inorder[:idx],postorder[idx:-1])
        # return root

        inorderIdx={v:i for i,v in enumerate(inorder)}
        def dfs(l,r):
            
            if l>r:
                return None
            

            root = TreeNode(postorder.pop())
            mid=inorderIdx[root.val]
           
            root.right=dfs(mid+1,r)
            root.left=dfs(l,mid-1)
            return root

        return dfs(0,len(inorder)-1)