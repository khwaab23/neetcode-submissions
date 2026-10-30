class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q=deque()
        visit=set(deadends)
        q.append("0000")
        steps=0
        if target == "0000":
            return 0
        if "0000" in visit:
            return -1

        while q:
            steps+=1
            for _ in range(len(q)):
                code=q.popleft()
                for i in range(4):
                    for j in [1,-1]:
                        digit=str((int(code[i])+j+10)%10)
                        nextcode=code[:i]+digit+code[i+1:]
                        if nextcode in visit:
                            continue
                        
                        if nextcode==target:
                            return steps
                        q.append(nextcode)
                        visit.add(nextcode)
        return -1
