class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for r in strs:
            res+=str(len(r))+'#'+r
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        i,j=0,0
        res=[]
        while j<len(s):
            while s[j]!='#':
                # print(s[j])
                j+=1
            length=int(s[i:j])
            print(length)
            i=j+1
            j=i+length
            res.append(s[i:j])
            i=j
        return res

