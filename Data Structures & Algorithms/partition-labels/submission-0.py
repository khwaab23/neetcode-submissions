class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last={}
        for i,c in enumerate(s):
            last[c]=i
        res=[]
        end=0
        size=0
        for i,c in enumerate(s):
            size+=1
            end=max(end,last[c])
            if end==i:
                res.append(size)
                size=0
                

        return res
