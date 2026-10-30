class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=[]
        carry=0 
        i,j=len(a)-1,len(b)-1
        while i>=0 or j>=0 or carry:
            int_A=int(a[i]) if i>=0 else 0
            int_B=int(b[j]) if j>=0 else 0

            total=int_A+int_B+carry
            res.append(total%2)
            carry=total//2
            j-=1
            i-=1

        res.reverse()
        return "".join(map(str,res))
        