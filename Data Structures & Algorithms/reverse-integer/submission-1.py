class Solution:
    def reverse(self, x: int) -> int:
        org=x
        res=int(str(abs(x))[::-1])
        if org<0:
            res=-res
        
        if res< - (1<<31) or res> (1<<31):
            return 0
        return res