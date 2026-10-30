class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate=range(1,max(piles))
        min_rate=max(piles)
        l=1
        r=max(piles)
        while l<=r:
            k=(l+r)//2
            hours=0
            print (k)
            for p in piles:
                hours+=math.ceil(float(p)/k)
            if hours<=h:
                min_rate=min(k,min_rate)
                r=k-1
            else:
                l=k+1
            
        return min_rate