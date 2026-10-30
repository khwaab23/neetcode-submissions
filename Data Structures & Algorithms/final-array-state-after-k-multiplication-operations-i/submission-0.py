class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        nums=[(val,i) for i,val in enumerate(nums)]
        res=[0]*len(nums)
        heapq.heapify(nums)

        for _ in range(k):
            x,i=heapq.heappop(nums)
            
            x*=multiplier
            heapq.heappush(nums,(x,i))
        
        for x,i in nums:
            res[i]=x
        
        return res
