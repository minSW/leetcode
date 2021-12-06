class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        prev = 0
        for start, end in sorted(intervals) :
            if prev > start : return False
            prev = end
        return True
