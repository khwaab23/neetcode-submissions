class MedianFinder:

    def __init__(self):
        self.minheap=[]

    def addNum(self, num: int) -> None:
        self.minheap.append(num)
        self.minheap.sort()

    def findMedian(self) -> float:
        n=len(self.minheap)-1
        mid=n//2
        if len(self.minheap)%2==0:

            return (self.minheap[mid]+self.minheap[mid+1])/2
        else:
            return float(self.minheap[n // 2])