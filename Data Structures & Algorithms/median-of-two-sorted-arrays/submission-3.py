class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1

        l,r=0,len(nums1)-1
        total=len(nums1)+len(nums2)
        halfLen=total//2

        while True:
            Alen=(l+r)//2
            Blen=halfLen-Alen-2

            Aleft=nums1[Alen] if Alen>=0 else float('-inf')
            Aright=nums1[Alen+1] if (Alen+1)<len(nums1) else float('inf')
            Bleft=nums2[Blen] if Blen>=0 else float('-inf')
            Bright=nums2[Blen+1] if (Blen+1)<len(nums2) else float('inf')

            if Aleft<=Bright and Aright>=Bleft:
                if total%2:
                    return min(Aright, Bright)
                return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                r=Alen-1
            else:
                l=Alen+1

