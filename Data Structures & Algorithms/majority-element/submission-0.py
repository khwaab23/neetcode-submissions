class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=defaultdict(int)
        maxnum,num=0,0
        for n in nums:
            count[n]+=1
            if maxnum<count[n]:
                maxnum=count[n]
                num=n
        return num
