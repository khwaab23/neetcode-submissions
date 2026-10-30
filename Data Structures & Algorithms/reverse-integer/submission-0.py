class Solution:
    def reverse(self, x: int) -> int:
        org=x
        x=abs(x)
        x=int(str(x)[::-1])
        if org<0:
            x*=-1
        if x<-2**31 or x>2**31:
            return 0
        else:
            return x