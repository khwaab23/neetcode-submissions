class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        maxheap=[[-cnt,val] for val,cnt in count.items()]
        heapq.heapify(maxheap)
        res=""
        prev=None
        while maxheap or prev:
            if prev and not maxheap:
                return ""
            cnt,val=heapq.heappop(maxheap)
            res+=val
            cnt+=1
            if prev:
                heapq.heappush(maxheap,prev)
                prev=None
            if cnt:
                prev=[cnt,val]
        
  
        return res
            

            