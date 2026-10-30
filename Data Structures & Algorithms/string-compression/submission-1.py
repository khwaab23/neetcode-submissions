class Solution:
    def compress(self, chars: List[str]) -> int:
        l,r=0,0
        current_char=chars[0]
        string=""
        while r<len(chars):
            
            while r<len(chars) and chars[r]==current_char:
                
                r+=1
            if r-l==1:
                string+=current_char
            else:
                string+=current_char+str(r-l)
            l=r
            current_char=chars[l] if l<len(chars) else None
        k=len(string)
        print(string)
        for i in range(min(len(string),len(chars))):
            chars[i]=string[i]
        return k
