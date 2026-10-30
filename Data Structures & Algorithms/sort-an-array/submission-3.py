class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums,0,len(nums)-1)
    
    def mergeSort(self,nums,s,e):
        if e-s+1<=1:
            return nums
        
        mid=(s+e)//2

        self.mergeSort(nums,s,mid)
        self.mergeSort(nums,mid+1,e)

        self.merge(nums,s,mid,e)
        return nums
    
    def merge(self,nums,s,m,e):
        i,j=0,0
        k=s

        L=nums[s:m+1]
        R=nums[m+1:e+1]

        while i<len(L) and j<len(R):
            if L[i]<=R[j]:
                nums[k]=L[i]
                i+=1
            else:
                nums[k]=R[j]
                j+=1
            k+=1
        
        while i < len(L):
            nums[k]=L[i]
            i+=1
            k+=1
        
        while j<len(R):
            nums[k]=R[j]
            j+=1
            k+=1
        return nums