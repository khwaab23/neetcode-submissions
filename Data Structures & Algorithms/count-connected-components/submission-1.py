class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={i:[] for i in range(n)}
        for src,dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        

        components=0
        visit=set()
        q=deque()

        def bfs(src):
            q.append(src)
            visit.add(src)
            while q:
                for i in range(len(q)):
                    node=q.popleft()
                    for nei in adj[node]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)        
        for src in adj:
            if src not in visit:
                bfs(src)
                components+=1
    
        return components


