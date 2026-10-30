class Solution:
    def scoreOfString(self, s: str) -> int:
        sum1=0
        n=len(s)
        i=1
        while i<n:
            sum1+=abs(ord(s[i])-ord(s[i-1]))
            i+=1
        return sum1
