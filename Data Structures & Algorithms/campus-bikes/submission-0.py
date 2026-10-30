class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        answer=defaultdict(list)
        minheap=[]
        for i,[xb,yb] in enumerate(bikes):
            for j,[xw,yw] in enumerate(workers):
                dist=abs(xb-xw)+abs(yb-yw)
                heapq.heappush(minheap,[dist,i,j])
        

        n=len(workers)
        bikes_Set=set()
        while len(answer)<n:
            dist,bike,worker=heapq.heappop(minheap)
            if worker in answer or bike in bikes_Set:
                continue  
            bikes_Set.add(bike)
            answer[worker]=bike
        res=[-1]*n
        for key,val in answer.items():
            res[key]=val
        
        return res