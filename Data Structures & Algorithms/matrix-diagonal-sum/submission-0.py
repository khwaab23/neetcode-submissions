class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows=len(mat)
        total=0
        visit=set()
        for i in range(rows):
            total+=mat[i][i]
            visit.add((i,i))

        for i in range(rows):
            if (i,rows-i-1) not in visit:
                total+=mat[i][rows-i-1]
        return total

            