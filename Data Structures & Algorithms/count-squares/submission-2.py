class CountSquares:

    def __init__(self):
        self.points=defaultdict(int)
        self.point1=[]
    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1
        self.point1.append(point)

    def count(self, point: List[int]) -> int:
        res=0
        px,py=point
        for x,y in self.point1:
            if abs(y-py)!=abs(x-px) or x==px or y==py:
                continue

            res+=self.points[(x,py)]*self.points[(px,y)]

        return res