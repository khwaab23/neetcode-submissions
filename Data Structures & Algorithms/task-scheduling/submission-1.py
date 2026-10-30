class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter=Counter(tasks)
        maxheap=[-cnt for cnt in counter.values()]

        heapq.heapify(maxheap)
        print(maxheap)
        q=deque()
        time=0
        while q or maxheap:
            time+=1
            
            if not maxheap:
                time=q[0][1]
            else:
                cnt=heapq.heappop(maxheap)
                cnt+=1
                if cnt:
                    q.append((cnt,time+n))

            if q and time==q[0][1]:
                cnt,time=q.popleft()
                heapq.heappush(maxheap,cnt)

        return time

