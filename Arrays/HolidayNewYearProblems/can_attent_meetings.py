'''
Given an array of meeting time intervals where intervals[i] = [starti, endi], 
determine if a person could attend all meetings.
'''
def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    def checkMeetingCollide(a, b):
        if (b[0] >= a[0] and b[0] < a[1]):
            return False

        if b[1] >= a[0] and b[1] <= a[1]:
            return False

        if b[0] <= a[0] and b[1] >= a[1]:
            return False

        if b[1] > a[1]:
            return b
        else:
            return a

    intervals.sort(key = lambda l:l[0])

    current = None
    for i in range(len(intervals)):
        if i == 0:
            current = intervals[i]
            continue

        current = checkMeetingCollide(current, intervals[i])

        if(current is False):
            return False

    return True
        