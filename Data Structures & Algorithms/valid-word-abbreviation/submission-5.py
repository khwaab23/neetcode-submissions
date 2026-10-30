class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w=0
        a=0
        m,n=len(word),len(abbr)
        if n==0:
            return False
        
        length=0
        while w<m and a<n:
            if abbr[a]=="0":
                return False
            if abbr[a].isdigit():
                r=a
                while r<n and abbr[r].isdigit():
                    r+=1
                length=int(abbr[a:r])
                a=r
                w+=length
                
                continue
            if w<m and a<n and word[w]!=abbr[a]:
                return False
            
            if w>m:
                return False
            
            

            w+=1
            a+=1


        return w== m and a == n