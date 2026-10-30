class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res=[[] for _ in range(numRows)]
        row=0
        dir=-1
        i=0
        while i<len(s):
            if row==0 or row==numRows-1:
                dir*=-1
            res[row].append(s[i])
            row+=dir
            i+=1
        
        return "".join("".join(row) for row in res)
