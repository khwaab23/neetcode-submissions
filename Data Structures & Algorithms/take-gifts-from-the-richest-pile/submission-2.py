class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=[-i for i in gifts]
        
        heapq.heapify(gifts)
        print(gifts)
        for _ in range(k):
            g=-heapq.heappop(gifts)
            heapq.heappush(gifts,-floor(sqrt(g)))
        return -int(sum(gifts))