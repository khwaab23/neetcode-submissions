class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        minheap=[]
        curpass=0
        for passs,start,end in trips:

            while minheap and minheap[0][0]<=start:
                curpass-=heapq.heappop(minheap)[1]
            
            curpass+=passs
            if curpass>capacity:
                return False
            
            heapq.heappush(minheap,[end,curpass])
        
        return True