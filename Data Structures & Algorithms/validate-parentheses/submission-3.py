class Solution:
    def isValid(self, s: str) -> bool:
        # closing={"}":"{","]":"[",")":"("}
        # stack=[]
        # for i in s:
        #     if i in closing:
        #         if stack and closing[i]==stack.pop():
        #             continue
        #         else:
        #             return False
        #     else:
        #         stack.append(i)

        # return True if not stack else False
        

        i=0
        stack=[]
        closing={")":"(","}":"{","]":"["}
        while i<len(s):
            if s[i] in closing:
                if not stack or closing[s[i]]!=stack.pop():
                    return False   
            else:
                stack.append(s[i])
            i+=1
        return True if not stack else False