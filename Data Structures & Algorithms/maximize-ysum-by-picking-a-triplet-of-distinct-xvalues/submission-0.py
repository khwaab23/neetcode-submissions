class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        mp={}
        for xi,yi in zip(x,y):
            mp[xi]=max(mp.get(xi,0),yi)
        minheap=[]
        for i in mp.values():
            heapq.heappush(minheap,i)
            if len(minheap)>3:
                heapq.heappop(minheap)
        
        return sum(minheap) if len(minheap)==3 else -1