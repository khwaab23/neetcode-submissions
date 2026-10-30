class HitCounter:

    def __init__(self):
        self.hits=[]

    def hit(self, timestamp: int) -> None:
        heapq.heappush(self.hits,timestamp)
        

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0]+300<=timestamp:
            heapq.heappop(self.hits)
        return len(self.hits)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
