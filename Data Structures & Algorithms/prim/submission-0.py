class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        
        adj={i:[] for i in range(n)}
        print(adj)
        for src,dst,wt in edges:
            adj[src].append([dst,wt])
            adj[dst].append([src,wt])
        
        res=0
        minheap=[[0,0]]
        visit=set()
    
        
        while minheap and len(visit)<n:

            w1,dst=heapq.heappop(minheap)
            if dst in visit:
                continue
            
            visit.add(dst)
            res+=w1
            for nei,w2 in adj[dst]:
                heapq.heappush(minheap,[w2,nei])

        return res if len(visit)==n else -1

