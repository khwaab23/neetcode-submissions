class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        q=deque()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==0:
                    q.append((r,c))
        
        while q:
            r,c=q.popleft()
            for i in range(len(matrix[0])):
                matrix[r][i]=0
            
            for i in range(len(matrix)):
                matrix[i][c]=0
        