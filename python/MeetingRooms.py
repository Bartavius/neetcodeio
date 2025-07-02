'''
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.
'''

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def canAttendMeetings(intervals) -> bool:

    sorted_intervals = sorted(intervals, key=lambda x: x.start)
    
    for i in range(len(sorted_intervals) - 1):
        if sorted_intervals[i].end > sorted_intervals[i + 1].start:
            return False
    return True