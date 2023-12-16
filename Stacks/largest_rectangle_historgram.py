"""
Given an array of integers A.

A represents a histogram i.e A[i] denotes the height of the ith histogram's bar. Width of each bar is 1.

Find the area of the largest rectangle formed by the histogram.
"""


def largest_rectangle_hist(A):
    N = len(A)

    small_left = [-1 for i in A]
    st = list()
    for i in range(N):
        while len(st) > 0 and st[-1][0] >= A[i]:
            st.pop()

        if len(st) == 0:
            small_left[i] = -1
        else:
            small_left[i] = st[-1][1]
        st.append((A[i], i))

    small_right = [N for i in A]
    st = list()
    for i in range(N - 1, -1, -1):
        while len(st) > 0 and st[-1][0] >= A[i]:
            st.pop()

        if len(st) == 0:
            small_right[i] = N
        else:
            small_right[i] = st[-1][1]
        st.append((A[i], i))

    max_area = 0
    for i in range(N):
        H = A[i]
        L = small_left[i]
        R = small_right[i]

        area = (R - L - 1) * H

        max_area = max(area, max_area)

    return max_area


assert largest_rectangle_hist([0, 2, 1]) == 2
