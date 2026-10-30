class Trie:
    def __init__(self):
        self.children={}
        self.word=False
    
    def addWord(self,word):
        cur=self
        for c in word:
            if c not in cur.children:
                cur.children[c]=Trie()
            cur=cur.children[c]
        cur.word=True
    
#children={b:{a:{t},a:[t,c],t:[a],c:[a]}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=Trie()
        for w in words:
            root.addWord(w)
        
        rows=len(board)
        cols=len(board[0])
        res=set()
        visit=set()
        
        def dfs(r,c,node,word):
            if min(r,c)<0 or r>=rows or c>=cols or (r,c) in visit or board[r][c] not in node.children:
                return 
            
            visit.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.word:
                res.add(word)
            
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
        

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")

        return list(res)
        
