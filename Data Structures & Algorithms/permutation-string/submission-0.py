class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        hash1={}
        for i in s1:
            hash1[i]=1+hash1.get(i,0)

        n=len(s1)

        def isValid(s2):
            hash2={}
            for i in s2:
                hash2[i]=1+hash2.get(i,0)
            return hash2
                    
        for i in range(len(s2)):
            if hash1==isValid(s2[i:i+n]):
                return True

        return False