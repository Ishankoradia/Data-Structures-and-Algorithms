"""
Given string A denoting an infix expression. Convert the infix expression into a postfix expression.

String A consists of ^, /, *, +, -, (, ) and lowercase English alphabets where lowercase English alphabets are operands and ^, /, *, +, - are operators.

Find and return the postfix expression of A.

NOTE:

^ has the highest precedence.
/ and * have equal precedence but greater than + and -.
+ and - have equal precedence and lowest precedence among given operators.

Example Input
Input 1:

A = "x^y/(a*z)+b"

Output 1:

"xy^az*/b+"
"""


def infix_to_postfix(A):
    st = list()
    ans = ""

    def rank(ch):
        if ch == "^":
            return 3
        elif ch == "/" or ch == "*":
            return 2
        elif ch == "+" or ch == "-":
            return 1
        else:
            return -1

    for ch in A:
        if ch not in ["^", "*", "/", "+", "-", "(", ")"]:
            ans += ch
        elif ch == "(":
            st.append(ch)
        elif ch == ")":
            # pop till '('
            temp = st.pop()
            while temp != "(":
                ans += temp
                temp = st.pop()
        else:  # operators
            while len(st) > 0 and rank(ch) <= rank(st[-1]):
                temp = st.pop()
                ans += temp
            st.append(ch)

    while len(st) > 0:
        temp = st.pop()
        ans += temp

    return ans


assert infix_to_postfix("x^y/(a*z)+b") == "xy^az*/b+"
