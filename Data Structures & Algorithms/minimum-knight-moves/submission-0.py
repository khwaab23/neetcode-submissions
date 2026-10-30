class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions=[[2,1],[1,2],[-2,1],[2,-1],[-2,-1],[-1,2],[-1,-2],[1,-2]]
        visit=set([(0, 0)])
        x, y = abs(x), abs(y)
        queue = deque([(0, 0, 0)])
        while queue:
            r, c, moves = queue.popleft()
            if r == x and c == y:
                return moves
            
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row, col) not in visit and -2 <= row <= x + 2 and -2 <= col <= y + 2:
                    visit.add((row, col))
                    queue.append((row, col, moves + 1))
        return 0