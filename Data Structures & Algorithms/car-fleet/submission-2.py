class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        pair=[(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)
        for pos,spd in pair:
            destination_time=(target-pos)/spd
            if not stack:
                stack.append(destination_time)
            if stack and stack[-1]<destination_time:
                stack.append(destination_time)
        return len(stack)


