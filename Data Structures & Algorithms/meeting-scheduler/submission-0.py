class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        timeslot=list(filter(lambda n: n[1]-n[0]>=duration,slots1+slots2))
        heapq.heapify(timeslot)
        while len(timeslot)>1:
            start1,end1=heapq.heappop(timeslot)
            start2,end2=timeslot[0]

            if end1>=start2+duration:
                return [start2,start2+duration]
        return []