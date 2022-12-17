"""
You have given a string A having Uppercase English letters.

You have to find how many times subsequence "AG" is there in the given string.

Note: Return the answer modulo 10^9 + 7 as the answer can be very large.
"""
def solve(self, A):
    cnt_a = 0
    ans = 0
    for x in A:
        if(x == 'A'):
            cnt_a += 1
        
        if(x == 'G'):
            ans += cnt_a

    return ans % (10**9 + 7)