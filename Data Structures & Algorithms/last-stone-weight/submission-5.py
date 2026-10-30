class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapq.heapify(stones)
        while stones and len(stones)>1:
            a,b=-heapq.heappop(stones),-heapq.heappop(stones)
            if a>b:
                heapq.heappush(stones,-(a-b))
        
        return -stones[0] if stones else 0 
