class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        satisfied=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                satisfied+=customers[i]
                customers[i]=0
        
        maxval=0
        l=0
        for r in range(minutes,len(customers)+1):
            maxval=max(maxval,sum(customers[l:r]))
            l+=1
        
        return satisfied+maxval