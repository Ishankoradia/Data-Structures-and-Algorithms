def solve( A):
    i = 1
    cnt = 0
    # factors come in pair, if i is a factor A/i is a factor too.
    # we only need to iterate through 1 to sqrt(A) since after these pairs are repeated
    while i * i <= A:
        if(A % i == 0):
            cnt += 1 if i == A/i else 2
        i += 1

    return cnt