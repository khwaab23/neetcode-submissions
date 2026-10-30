class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students=defaultdict(list)
        for sid,marks in items:
            heapq.heappush(students[sid],-marks)
        
        res=[]
        for sid in students:
            k=5
            total=0
            
            while students[sid] and k>0:
                total+=(-heapq.heappop(students[sid]))
                k-=1
            heapq.heappush(res,[sid,total//5-k])
        return res
