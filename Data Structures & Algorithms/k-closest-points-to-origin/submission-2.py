class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nums=[]
        for x,y in points:
            distance=(x)**2 + (y)**2
            nums.append([distance,x,y])
        heapq.heapify(nums)
        res=[]
        for i in range(k):
            distance,x,y=heapq.heappop(nums)
            res.append([x,y])
        return res