"""
Imagine you're a teacher. You ask students to call out a letter one by one. 
After each letter, you jot down the very first letter that's only been called out once. 
If all letters have been repeated, you write "#".

Here's a scenario:

A student says "a". It's the first letter. You write "a".
Next, a student says "b", "a" is still unique, so you add "a". Now it's "aa".
A student says "a" again. Now, "b" is the unique one. You add "b", making it "aab".
A student says "b". All letters so far are repeated. You add "#". It becomes "aab#".
A student says "c". "c" is unique. You add "c". The final is "aab#c".
Your task? Given the sequence the students call out A, determine the string on the board.

Example Input
Input 1:

 A = "abadbc"

Output 1: "aabbdd"

"a"      -   first non repeating character 'a'
"ab"     -   first non repeating character 'a'
"aba"    -   first non repeating character 'b'
"abad"   -   first non repeating character 'b'
"abadb"  -   first non repeating character 'd'
"abadbc" -   first non repeating character 'd'

"""
from collections import deque


def solve(A):
    ans = ""
    q = deque()
    d = dict()
    for i in range(len(A)):
        if A[i] not in d:
            q.append(A[i])

        d[A[i]] = d.get(A[i], 0) + 1

        while len(q) > 0 and d[q[0]] > 1:
            q.popleft()

        if len(q) > 0:
            ans = ans + q[0]
        else:
            ans = ans + "#"

    return ans
