"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], 
obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, 
return the maximum profit you can take such that there are no two jobs 
in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

DoorDash, Urban Company, Pinterest
"""


def jobScheduling(startTime: list, endTime: list, profit: list) -> int:
    """TC: O(NlogN) SC: O(N)"""
    N = len(startTime)

    arr = [(startTime[i], endTime[i], profit[i]) for i in range(N)]
    arr.sort(key=lambda x: x[0])

    global dp
    dp = [-1 for i in range(N)]

    def find_next_curr(last_ending_time, arr):
        start = 0
        end = len(arr) - 1
        next_curr = len(arr)

        while start <= end:
            mid = (start + end) // 2
            if arr[mid][0] >= last_ending_time:
                next_curr = mid
                end = mid - 1
            else:
                start = mid + 1

        return next_curr

    def maxProfit(curr, arr=arr):
        global dp
        if curr == len(arr):
            return 0

        if dp[curr] != -1:
            return dp[curr]

        # dont consider the current job
        f1 = maxProfit(curr + 1)

        next_curr = find_next_curr(arr[curr][1], arr)

        f2 = arr[curr][2]
        if next_curr >= 0 and next_curr < len(arr):
            f2 += maxProfit(next_curr)

        dp[curr] = max(f1, f2)

        return dp[curr]

    return maxProfit(0)
