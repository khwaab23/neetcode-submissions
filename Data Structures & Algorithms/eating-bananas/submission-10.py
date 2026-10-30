class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==h:
            return max(piles)
        
        l,r=1,max(piles)
        min_k=float('inf')
        while l<=r:
            hours=0
            k=(l+r)//2
            for p in piles: 
                hours+=math.ceil(p/k)

            if hours<=h:
                min_k=min(min_k,k)
                r=k-1
            else:
                l=k+1
        return min_k

