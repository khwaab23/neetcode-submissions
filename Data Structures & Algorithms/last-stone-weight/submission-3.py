class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            stone1,stone2=-heapq.heappop(stones),-heapq.heappop(stones)
            if abs(stone1-stone2)!=0:
                heapq.heappush(stones,-(stone1-stone2))
            
        return -stones[0] if len(stones)==1 else 0