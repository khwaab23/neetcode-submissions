class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count=0
        stack=[]
        i=0
        popped=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            
            elif s[i]==')':
                if stack:
                    stack.pop()

                else:
                    popped.append(i)
        while stack:
            popped.append(stack.pop())    
        result = "".join( s[i] for i in range(len(s)) if i not in popped)

        return result
                