class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash1={}
        freq=[[] for _ in range(len(nums)+1)]
        for i in nums:
            hash1[i]=1+hash1.get(i,0)
        print(hash1)
        print(freq)
        for num,cnt in hash1.items():
            freq[cnt].append(num)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res