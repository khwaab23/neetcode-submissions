# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"
        
        q=deque()
        q.append(root)
        res=[]
        while q:
            for i in range(len(q)):
                node=q.popleft()
                res.append(str(node.val) if type(node)==TreeNode else "#")

                if type(node)==TreeNode:
                    if node.left:
                        q.append(node.left)
                    else:
                        q.append("#")

                    if node.right:
                        q.append(node.right)
                    else:
                        q.append("#")   
       
        return ",".join(res)     
        


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data=data.split(",")
        if data[0]=="#":
            return None
        
      
      
        root=TreeNode(data[0])
        q=deque([root])
        index=1
        while q:
            node=q.popleft()
            if data[index]!="#":
                node.left=TreeNode(data[index])
                q.append(node.left)
            
            index+=1
            if data[index]!="#":
                node.right=TreeNode(data[index])
                q.append(node.right)
            index+=1
        return root

