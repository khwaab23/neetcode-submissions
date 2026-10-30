class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops="+-*/"
        stack=[]
        for i in tokens:
            
            if i=='+':
                a,b=int(stack.pop()),int(stack.pop())
                stack.append(a+b)
            elif i=='-':
                b,a=int(stack.pop()),int(stack.pop())
                stack.append(a-b)
            elif i=='*':
                b,a=int(stack.pop()),int(stack.pop())
                stack.append(b*a)
            elif i=='/':
                b,a=int(stack.pop()),int(stack.pop())
                stack.append(int(float(a)/b))
            else:
                stack.append(int(i))
        return stack[0]