class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        #We will use prims algorithm
        #since we need maximum probability, we will use a maxheap

        adj=defaultdict(list)
        for i,edge in enumerate(edges):
            a,b=edge
            adj[a].append([b,succProb[i]])
            adj[b].append([a,succProb[i]])
        print(adj)
        visit=set()
        res=1
        heap=[[-1,start_node]]
        while heap:
            prob,node=heapq.heappop(heap)
            visit.add(node)
            # prob=-prob
            if end_node==node:
                return -prob
            
            for node2,prob2 in adj[node]:
                if node2 not in visit:
                    heapq.heappush(heap,[prob*prob2,node2])
        return 0



