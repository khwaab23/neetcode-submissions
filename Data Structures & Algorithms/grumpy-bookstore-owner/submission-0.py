class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied=0
        
        for i in range(len(customers)):
            if grumpy[i]==0:
                satisfied+=customers[i]
                customers[i]=0

        
        # [0,0,0,2,0,1,0,5]
        maxsum=window=sum(customers[:minutes])
        i,j=0,minutes
        while j<len(customers):
            window=window-customers[i]+customers[j]
            maxsum=max(window,maxsum)
            i+=1
            j+=1
        
        
        return satisfied+maxsum
        