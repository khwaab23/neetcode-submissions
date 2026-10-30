class RandomizedSet:

    def __init__(self):
        self.set=[]
        self.setmap={}

    def insert(self, val: int) -> bool:
        if val in self.setmap:
            return False
        
        self.setmap[val]=len(self.set)
        self.set.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.setmap:
            return False
        idx=self.setmap[val]
        self.setmap[self.set[-1]]=idx
        self.set[idx]=self.set[-1]
        del self.setmap[val]
        self.set.pop()
        return True
        

    def getRandom(self) -> int:
        idx=random.randint(0,len(self.set)-1)
        return self.set[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()