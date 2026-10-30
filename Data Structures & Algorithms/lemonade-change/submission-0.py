class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0]!=5:
            return False
        register={5:0,10:0,20:0}
        for bill in bills:
            if bill==5:
                register[5]+=1
                continue
            elif bill==10:
                if register[5]<=0:
                    return False
                register[5]-=1
                register[10]+=1
            else:
                if register[10] > 0 and register[5] > 0:
                    register[10]-=1
                    register[5]-=1
                elif register[5] >= 3:
                    register[5]-=3
                else:
                    return False
                register[20]+=1
        return True