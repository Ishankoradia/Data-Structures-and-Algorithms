"""
Given an Integer A. Return 1 if A is prime and return 0 if not.
"""
def solve( A):
    i = 1
    cnt = 0
    # count all factors of the number A
    # If unique count of factors is exactly 2 then its a prime number else not
    while i * i <= A:
        if(A % i == 0):
            cnt += 1 if i == A/i else 2
            if cnt > 2:
                return 0
        i += 1            

    return 1 if cnt == 2 else 0