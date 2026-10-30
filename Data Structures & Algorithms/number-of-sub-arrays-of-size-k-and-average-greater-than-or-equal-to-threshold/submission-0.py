class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res=0
        l=0
        sum1=0
        for r in range(len(arr)):
            sum1+=arr[r]

            if r-l+1==k:
                if sum1/k>=threshold:
                    res+=1  
                sum1-=arr[l]
                l+=1
        return res

