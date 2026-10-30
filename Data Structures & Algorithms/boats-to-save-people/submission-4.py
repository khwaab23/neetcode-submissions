class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res,l,r=0,0,len(people)-1
        people.sort()
        while l<=r:
            remain=limit-people[r]
            r-=1
            res+=1
            if l<=r and people[l]<=remain:
                l+=1
        return res