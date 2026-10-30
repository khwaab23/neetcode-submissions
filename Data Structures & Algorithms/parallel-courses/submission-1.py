class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj= {i:[] for i in range(1,n+1)}
        for pre, crs in relations:
            adj[pre].append(crs)
        
        visit={}

        def dfs(pre):
            if pre in visit:
                return visit[pre]

            visit[pre]=-1

            maxlen=1
            for crs in adj[pre]:
                length=dfs(crs)
                if length==-1:
                    return -1
                maxlen=max(length+1,maxlen)
            visit[pre]=maxlen
            return maxlen

        maxlen=-1
        for i in adj.keys():
            length=dfs(i)
            if length==-1:
                return -1
            maxlen=max(maxlen,length)
        return maxlen
