import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=[-i for i in gifts]
        heapq.heapify(gifts)
        for i in range(k):
            maxgift=-heapq.heappop(gifts)
            heapq.heappush(gifts,-floor(math.sqrt(maxgift)))
        
        total=sum(gifts)
        return -total