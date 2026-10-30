class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj={}
        for i in range(1,n+1):
            adj[i]=[]

        for src,dst,wei in times:
            adj[src].append((wei,dst))
        
        minheap=[(0,k)]

        shortest={}
        while minheap:
            w1,n1 =heapq.heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1]=w1

            for w2,n2 in adj[n1]:
                if n2 in shortest:
                    continue
                heapq.heappush(minheap,(w1+w2,n2))
        print(adj)
        print(shortest)
        return max(shortest.values()) if len(shortest)==n else -1

            

