class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        for x,y in points:
            x1=x**2
            y1=y**2
            res.append([x1+y1,x,y])
        heapq.heapify(res)
        res1=[]
        for _ in range(k):
            d,x,y=heapq.heappop(res)
            res1.append([x,y])
        return res1

