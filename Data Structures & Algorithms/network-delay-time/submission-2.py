class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        for i in range(1,n+1):
            adj[i]=[]

        for u,v,t in times:
            adj[u].append([v,t])
        
        minheap=[[0,k]]
        shortest={}
        while minheap:
            t,u=heapq.heappop(minheap)
            if u in shortest:
                continue
            shortest[u]=t

            for v,t1 in adj[u]:
                if v not in shortest:
                    heapq.heappush(minheap,[t+t1,v])
        print(shortest)
        return max(shortest.values()) if len(shortest)==n else -1