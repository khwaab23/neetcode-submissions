class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        total=0
        while len(sticks)>1:
            a=heapq.heappop(sticks)
            b=heapq.heappop(sticks)
            total+=a+b
            heapq.heappush(sticks,a+b)

        return total
