class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        l = len(self.stack)
        s = self.stack[(l-1)]
        return s
        

    def getMin(self) -> int:
        min = self.stack[0]
        for x in self.stack:
            if(x<min):
                min = x
        return min 
