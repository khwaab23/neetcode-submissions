class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for a in asteroids:
            if not stack or a>0:
                stack.append(a)
            
            else:
                while a<0 and stack:
                    if stack[-1]>0:
                        if abs(a)>stack[-1]:
                            stack.pop()
                        elif abs(a)==stack[-1]:
                            stack.pop()
                            a=0
                            break
                        else:
                            a=0
                    elif stack[-1]<0:
                        stack.append(a)
                        break
                    if not stack and a != 0:
                        stack.append(a)
                        break
        return stack