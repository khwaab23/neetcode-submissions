class Solution:
    def isValid(self, s: str) -> bool:
        closing={")":"(","}":"{","]":"["}
        stack=[]
        for r in s:
            if r in closing:
                if not stack or closing[r]!=stack.pop():
                    return False
            else:
                stack.append(r)
        return True if not stack else False

