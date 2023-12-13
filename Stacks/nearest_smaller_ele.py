"""
Given an array A, find the nearest smaller element G[i] for every element A[i] in the array 
such that the element has an index smaller than i.

More formally,

G[i] for an element A[i] = an element A[j] such that

j is maximum possible AND

j < i AND

A[j] < A[i]

Elements for which no smaller element exist, consider the next smaller element as -1.
"""


def nearest_smaller(A):
    N = len(A)
    st = list()

    G = [-1 for i in range(N)]
    for i in range(N):
        while len(st) > 0 and st[-1] >= A[i]:
            st.pop()

        if len(st) == 0:
            G[i] = -1
        else:
            G[i] = st[-1]

        st.append(A[i])

    return G
