class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        hash1={}
        for i in range(1,n+1):
            hash1[i]=0
        
        for n in nums:
            hash1[n]+=1
        
        res=[]
        for key,val in hash1.items():
            if val==0:
                res.append(key)
        return res