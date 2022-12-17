"""
A wire connects N light bulbs.

Each bulb has a switch associated with it; however, due to faulty wiring, 
a switch also changes the state of all the bulbs to the right of the current bulb.

Given an initial state of all bulbs, 
find the minimum number of switches you have to press to turn on all the bulbs.

You can press the same switch multiple times.

Note: 0 represents the bulb is off and 1 represents the bulb is on.
"""
def bulbs(self, A):
    cnt = 0
    for i in range(len(A)):
        if (A[i] == 1 and cnt % 2 == 0) or (A[i] == 0 and cnt % 2 == 1):
            continue

        cnt += 1

    return cnt