class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj={}
        truster=[False]*(n+1)
        for i in range(1,n+1):
            adj[i]=[]
        for a,b in trust:
            adj[b].append(a)
            truster[a]=True
        
        for i in range(1,n+1):
            if len(adj[i])==n-1 and not truster[i]:
                return i

        return -1
        
        