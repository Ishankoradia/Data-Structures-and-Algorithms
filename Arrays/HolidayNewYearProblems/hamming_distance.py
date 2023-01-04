'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
'''
def hammingDistance(self, x: int, y: int) -> int:
    num = x^y
    dist = 0
    while num > 0:
        digit = num % 2
        num = num // 2
        if digit == 1:
            dist += 1

    return dist