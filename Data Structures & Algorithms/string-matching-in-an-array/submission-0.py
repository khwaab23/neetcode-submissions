class TreeNode:
    def __init__(self):
        self.children={}
        self.cnt=0

class Trie:
    def __init__(self):
        self.root=TreeNode()
    
    def insert(self,word):
        for i in range(len(word)):
            cur=self.root
            for c in word[i:]:
                if c not in cur.children:
                    cur.children[c]=TreeNode()
                cur=cur.children[c]
                cur.cnt+=1

    def search(self,word):
        cur=self.root
        for c in word:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return True if cur.cnt>1 else False
        

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        trie=Trie()
        for word in words:
            trie.insert(word)
        
        for word in words:
            if trie.search(word):
                res.append(word)
        return res
        