class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n=len(customers)
        satisfied=0
        for i in range(n):
            if grumpy[i]==0:
                satisfied+=customers[i]
                customers[i]=0
        print(customers)
        max_satisfied=satisfied
        cc=satisfied
        l=0
        for r in range(n):
            cc+=customers[r]

            if r-l+1==minutes:
                max_satisfied=max(cc,max_satisfied)
                cc-=customers[l]
                l+=1
            
            
        return max_satisfied

