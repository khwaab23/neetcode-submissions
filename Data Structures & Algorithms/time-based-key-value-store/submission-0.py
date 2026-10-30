class TimeMap:

    def __init__(self):
        self.keyStore={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.keyStore:
            self.keyStore[key]=[]

        self.keyStore[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.keyStore:
            return ""
        l,r=0,len(self.keyStore[key])-1
        res=""
        values=self.keyStore.get(key)
        
        while l<=r:
            mid=(l+r)//2
            if values[mid][1]<=timestamp:
                l=mid+1
                res=values[mid][0]
            else:
                r=mid-1
        
        return res
            

