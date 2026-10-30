"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i : i.start)
        if not intervals:
            return True
        prevEnd=intervals[0].end 
        for i in intervals[1:]:
            if i.start<prevEnd:
                return False
            prevEnd=i.end
        return True