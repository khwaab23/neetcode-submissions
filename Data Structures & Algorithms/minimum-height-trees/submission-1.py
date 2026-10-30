class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        minh=0
        minimum=float('inf')
        def bfs(root):
            q=deque()
            q.append(root)
            visit=set()
            visit.add(root)
            height=0
            while q:
                for _ in range(len(q)):
                    node=q.popleft()
                    for nei in adj[node]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
                height+=1
            return height

        res=[]
        for i in range(n):
            minh=bfs(i)
            minimum=min(minh,minimum)
            res.append((minh,i))
        print(res)

        final=[]
        for minh,i in res:
            if minh==minimum:
                final.append(i)
            
        return final