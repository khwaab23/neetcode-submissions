class TimeMap:

    def __init__(self):
        self.keyStore=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key]=[]
        self.keyStore[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.keyStore:
            return ""
        
        l,r=0,len(self.keyStore[key])-1
        res=""
        values=self.keyStore[key]
        while l<=r:
            mid=(l+r)//2
            if timestamp<values[mid][0]:
                r=mid-1
            else:
                l=mid+1
                res=values[mid][1]
        
        return res
        
