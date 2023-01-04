'''
Given an integer num, return a string representing its hexadecimal representation. 
For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, 
and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.
'''
def toHex(self, num: int) -> str:
    d = {}
    d[10] = "a"
    d[11] = "b"
    d[12] = "c"
    d[13] = "d"
    d[14] = "e"
    d[15] = "f"
    hex_str = ""
    if num == 0:
        return "0"

    if num < 0:
        num = 2**32 + num

    while num > 0:
        digit = num % 16
        num = num // 16
        if digit >= 10:
            digit = d[digit]

        hex_str = str(digit) + hex_str

    return hex_str