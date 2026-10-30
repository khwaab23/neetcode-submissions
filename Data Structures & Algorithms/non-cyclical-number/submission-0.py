class Solution:
    def isHappy(self, n: int) -> bool:
        
        visit=set()
        def squares(n):
            n=[int(i) for i in list(str(n))]
            total=0
            for num in n:
                total+=num**2
            return total

        def answer(n):
            while True:
                total=squares(n)
                if total==1:
                    return True
                if total in visit:
                    return False
                visit.add(total)

                return answer(total)

        return answer(n)
        