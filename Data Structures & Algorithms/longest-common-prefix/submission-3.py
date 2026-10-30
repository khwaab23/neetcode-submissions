class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # minLen=float('inf')
        # for w in strs:
        #     minLen=min(len(w),minLen)
        # n=len(strs)
        # # res=0
        # for i in range(len(strs[0])):
        #     for w in strs:
        #         if i==len(w) or w[i]!=strs[0][1]:
        #             return w[:i]

        # return strs[0]
        
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]