class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        for x,y in points:
            x1=x**2
            y1=y**2
            distance=(x1+y1)
            heapq.heappush(minheap,[distance,x,y])
        res=[]
        for _ in range(k):
            dist,x,y=heapq.heappop(minheap)
            res.append([x,y])
        return res
