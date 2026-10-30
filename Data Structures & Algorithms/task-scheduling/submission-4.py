class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        minheap=[-cnt for cnt in count.values()]
        heapq.heapify(minheap)
        time=0
        q=deque()

        while minheap or q:
            time+=1
            if not minheap:
                time=q[0][1]
            
            else:
                cnt=heapq.heappop(minheap)
                cnt+=1
                if cnt:
                    q.append([cnt,time+n])
            
            if q and q[0][1]<=time:
                cnt,time=q.popleft()
                heapq.heappush(minheap,cnt)
        
        return time
