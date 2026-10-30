class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            if i>0 and nums[i-1]==nums[i]:
                continue
            while j<k:
                sum1=nums[i]+nums[j]+nums[k]

                if sum1>0:
                    k-=1
                elif sum1<0:
                    j+=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
        print(res)
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        res=[]
        nums.sort()
        for i in range(len(nums)-2):
            j,k=i+1,len(nums)-1
            if i>0 and nums[i-1]==nums[i] :
                continue
            while j<k:
                s=nums[i]+nums[j]+nums[k]

                if s>0:
                    k-=1
                if s<0:
                    j+=1
                
                elif s==0:
                    res.append([nums[i],nums[j],nums[k]])
                    k-=1
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1

        return res
