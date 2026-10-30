class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda n: n[0])
        CI=intervals[0]
        res=[]
        for j in range(len(intervals)):
            s1,e1=CI
            s,e=intervals[j]
            if e1<s:
                res.append(intervals[j])
                CI=intervals[j]
            else:
                if res:res.pop()
                CI=[min(s1,s),max(e,e1)]
                res.append(CI)

        return res            
