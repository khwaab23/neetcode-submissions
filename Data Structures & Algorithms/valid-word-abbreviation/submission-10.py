class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        res=""
        i=0
        while i<len(abbr):
            if abbr[i].isdigit():
                if abbr[i]=='0':
                    return False
                length=""
                while i<len(abbr) and abbr[i].isdigit():
                    length+=abbr[i]
                    i+=1

                res+="*"*int(length)
            else:
                res+=abbr[i]
                i+=1
        
        if len(res)!=len(word):
            return False

        for i in range(len(word)):
            if not (word[i]==res[i] or res[i]=="*"):
                return False
        
        return True