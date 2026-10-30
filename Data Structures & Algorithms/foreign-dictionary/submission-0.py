class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj={c:set() for w in words for c in w}
        res=[]
        
        path=set()

        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            minlen=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minlen]==w2[:minlen]:
                return ""

            for j in range(minlen):
                if w1[j]==w2[j]:
                    continue
                adj[w1[j]].add(w2[j])
                break

        visited={}
        def dfs(src):
            if src in visited:
                return visited[src]

            visited[src]=True
            

            for nei in adj[src]:
                if dfs(nei):
                    return True
            
            res.append(src)
            visited[src]=False

        for src in adj:
            if dfs(src):
                return ""

        res.reverse()
        return "".join(res)
            
