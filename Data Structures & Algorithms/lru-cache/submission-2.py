class LRUCache:

    def __init__(self, capacity: int):
        self.capacity= capacity
        self.keyStore=OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.keyStore:
            return -1
        self.keyStore.move_to_end(key)
        return self.keyStore[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.keyStore:
            self.keyStore.move_to_end(key)
        self.keyStore[key]=value
        if len(self.keyStore)>self.capacity:
            self.keyStore.popitem(last=False)
        
