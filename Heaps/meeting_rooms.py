"""
Given an 2D integer array A of size N x 2 denoting time intervals of different meetings.

Where:

A[i][0] = start time of the ith meeting.
A[i][1] = end time of the ith meeting.

Find the minimum number of conference rooms required so that all meetings can be done.

Note :- If a meeting ends at time t, another meeting starting at time t can use the same conference room

"""
from functools import cmp_to_key
import heapq


# using arrays
def array_solve(A):
    N = len(A)  # no of meetings

    def compare(t1, t2):
        if t1 and t2:
            if t1[0] < t2[0]:
                return -1
            elif t1[0] > t2[0]:
                return 1
            elif t1[0] == t2[0]:
                if t1[1] == "s" and t2[1] == "e":
                    return 1
                elif t1[1] == "e" and t2[1] == "s":
                    return -1
                return 0

    times = []
    for x in A:
        times.append((x[0], "s"))
        times.append((x[1], "e"))

    times.sort(key=cmp_to_key(compare))

    ans = 0
    max_consecutive = 0

    for t in times:
        if t[1] == "s":
            if max_consecutive >= ans:
                ans += 1
            max_consecutive += 1
        else:
            if max_consecutive > 0:
                max_consecutive -= 1

    return ans


# using priority queue / heaps
def heap_solve(A):
    A.sort(key=lambda x: x[0])

    N = len(A)

    end_times = []
    heapq.heapify(end_times)

    heapq.heappush(end_times, A[0][1])

    # idea is to check if some room is occupied or not ; if not assign the same room to a meeting
    for i in range(1, N):
        if end_times[0] <= A[i][0]:
            heapq.heappop(end_times)

        heapq.heappush(end_times, A[i][1])

    return len(end_times)
