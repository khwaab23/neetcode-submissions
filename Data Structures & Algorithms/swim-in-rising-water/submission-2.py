class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        visit=set()
        visit.add((0,0))
        time=0
        shortest={}
        minheap=[[grid[0][0],(0,0)]]
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        
        while minheap:
            wt,(r,c)=heapq.heappop(minheap)
            if (r,c) in shortest:
                continue
            time=max(time,wt)
            shortest[(r,c)]=wt
            if r==rows-1 and c==cols-1:
                return time
            
            for dr,dc in directions:
                row=dr+r
                col=dc+c

                if min(row,col)<0 or row>=rows or col>=cols:
                    continue
                
                if (row,col) not in visit:
                    heapq.heappush(minheap,[grid[row][col],(row,col)])
                    visit.add((row,col))
        
 

