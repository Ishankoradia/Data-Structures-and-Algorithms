"""
Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'.

Check whether A has redundant braces or not.

NOTE: A will be always a valid expression and will not contain any white spaces.

Return 1 if A has redundant braces else, return 0.
"""


def braces(A):
    st = list()

    for ch in A:
        if ch == ")":
            num = 0
            temp = st.pop()
            while temp != "(":
                num += 1
                temp = st.pop()

            if num <= 1:  # () or (a)
                return 1
        else:
            st.append(ch)

    return 0


assert braces("(A)") == 1
assert braces("(A*(A))") == 1
