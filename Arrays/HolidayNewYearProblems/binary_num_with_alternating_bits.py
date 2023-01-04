'''
Given a positive integer, check whether it has alternating bits: 
namely, if two adjacent bits will always have different values.
'''
def hasAlternatingBits(self, n: int) -> bool:
    b = None
    while n > 0:
        digit = n % 2
        n = n // 2
        if b is None:
            b = digit
        else:
            if digit ^ b != 1:
                return False

            b = digit


    return True
