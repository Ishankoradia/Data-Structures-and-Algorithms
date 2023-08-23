"""
You are given an array A of integers that represent the lengths of ropes.

You need to connect these ropes into one rope. The cost of joining two ropes equals the sum of their lengths.

Find and return the minimum cost to connect these ropes into one rope.
"""
import heapq


def connect_ropes(arr: list):
    """Functon"""
    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        return arr[0]

    heapq.heapify(arr)

    cost = 0

    while len(arr) > 1:
        min1 = heapq.heappop(arr)
        min2 = heapq.heappop(arr)

        cost += min1 + min2

        # append the merged rope of min1 & min2
        heapq.heappush(arr, min1 + min2)

    return cost


assert connect_ropes([1, 2, 3, 4, 5]) == 33
assert connect_ropes([5, 17, 100, 11]) == 182
