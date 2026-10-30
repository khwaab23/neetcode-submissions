class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        row_arr=[0]*(rows)
        col_arr=[0]*(cols)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:

                    row_arr[r]+=1
                    col_arr[c]+=1
        res=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and max(row_arr[r],col_arr[c])>1:
                    res+=1


        return res
