class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash1={}

        for num in nums:
            hash1[num]=1+hash1.get(num,0)

        freq=[[] for _ in range(len(nums)+1)]
        for val,cnt in hash1.items():
            freq[cnt].append(val)
        
        res=[]

        for i in range(len(freq)-1,-1,-1):
            for j in freq[i]:
                res.append(j)

                if len(res)==k:
                    return res

