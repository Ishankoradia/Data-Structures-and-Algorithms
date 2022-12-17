"""
You are given an integer A. You have to tell whether it is a perfect number or not.

Perfect number is a positive integer which is equal to the sum of its proper positive divisors.

A proper divisor of a natural number is the divisor that is strictly less than the number.
"""
def solve( A):
    i = 2
    sum1 = 1
    while i * i <= A:

        if(A % i == 0):
            sum1 += i + (A / i) if i != A/i else i
        
        if(sum1 > A):
            return 0
        
        i+=1

    return 1 if (A != 1 and sum1 == A) else 0