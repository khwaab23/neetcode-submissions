class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashs,hasht=Counter(s),Counter(t)

        for c in t:
            if c not in hashs or hashs[c]<hasht[c]:
                return c