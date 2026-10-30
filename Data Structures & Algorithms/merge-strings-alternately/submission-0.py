class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1=list(word1)
        word2=list(word2)
        minlen=min(len(word1),len(word2))
        res=""
        for i in range(minlen):
            res+=word1[i]+word2[i]
        return res+"".join(word1[minlen:])+"".join(word2[minlen:])