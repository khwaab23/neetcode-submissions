class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        preflen=len(pref)
        res=0
        for word in words:
            if word[:preflen]==pref:
                res+=1
        return res