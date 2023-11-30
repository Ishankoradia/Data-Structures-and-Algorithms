"""
You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] 
means that a meeting will be held during the half-closed time interval [starti, endi). 
All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

1. Each meeting will take place in the unused room with the lowest number.

2. If there are no available rooms, the meeting will be delayed until a room becomes free. 
The delayed meeting should have the same duration as the original meeting.

3. When a room becomes unused, meetings that have an earlier original start time should be given the room.

Return the number of the room that held the most meetings. 
If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.

"""
from typing import List
import heapq


def mostBooked(n: int, meetings: List[List[int]]) -> int:
    rooms = [i for i in range(n)]
    heapq.heapify(rooms)
    booked = [0 for _ in range(n)]

    end_times = []
    heapq.heapify(end_times)

    # sort by start time
    meetings.sort(key=lambda x: x[0])

    # assign/start the first meeting
    room = heapq.heappop(rooms)
    heapq.heappush(end_times, (meetings[0][1], room))  # (end_time, room)
    booked[room] += 1

    for i in range(1, len(meetings)):
        interval = meetings[i][1] - meetings[i][0]
        current_end = meetings[i][1]

        while len(end_times) > 0 and end_times[0][0] <= meetings[i][0]:
            (end, room) = heapq.heappop(end_times)
            # room becomes unused
            heapq.heappush(rooms, room)

        if len(rooms) == 0:
            (end, room) = heapq.heappop(end_times)
            # room becomes unused
            heapq.heappush(rooms, room)
            # delay the current meeting
            current_end = end + interval

        room = heapq.heappop(rooms)
        heapq.heappush(end_times, (current_end, room))  # (end_time, room)
        booked[room] += 1

    ans = n
    bookings = 0
    for i in range(len(booked)):
        if booked[i] > bookings:
            ans = i
            bookings = booked[i]

    return ans
