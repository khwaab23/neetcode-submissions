class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash1=defaultdict(list)
        for s in strs:
            sorted_s="".join(sorted(s))
            hash1[sorted_s].append(s)
        print(hash1.values())
        return list(hash1.values())
