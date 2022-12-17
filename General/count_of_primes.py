"""
You will be given an integer n. You need to return the count of prime numbers less than or equal to n.
"""
def solve( A):
    cnt = 0
    for n in range(2, A+1):
        i = 1
        cnt_f = 0
        is_prime = True 
        while i * i <= n:
            
            if(n % i == 0):
                cnt_f += 2 if i != n/i else 1 

            i += 1

            if(cnt_f > 2):
                is_prime = False
                break

        cnt += 1 if is_prime else 0