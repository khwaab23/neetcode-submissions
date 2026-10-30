class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pending=[]
        available=[]
        time=0
        res=[]
        for i,(enq,proc) in enumerate(tasks):
            heapq.heappush(pending,(enq,proc,i))
        
        while pending or available:

            while pending and pending[0][0]<=time:
                enq,proc,i=heapq.heappop(pending)
                heapq.heappush(available,(proc,i))

            if not available:
                time=pending[0][0]
                continue
            
            proc,i=heapq.heappop(available)
            res.append(i)
            time+=proc

        return res

            
        