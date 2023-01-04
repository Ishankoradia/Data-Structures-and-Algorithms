'''
You have a set of integers s, which originally contains all the numbers from 1 to n. 
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set,
which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array
'''
def findErrorNums(self, nums: List[int]) -> List[int]:
    xor = 0
    for i in nums:
        xor = xor ^ i

    for i in range( len(nums)):
        xor = xor ^ (i+1)

    mul = 1
    pos = 0
    while xor & mul == 0:
        pos += 1
        mul = 1 << pos

    xor1 = 0
    xor2 = 0

    for i, ele in enumerate(nums):
        if (i+1) & mul == 0:
            xor1 = xor1 ^ (i+1)
        else:
            xor2 = xor2 ^ (i+1)


        if ele & mul == 0:
            xor1 = xor1 ^ ele
        else:
            xor2 = xor2 ^ ele

    cnt1 = 0
    cnt2 = 0
    for i in nums:
        if i == xor1:
            cnt1 += 1

        if i == xor2:
            cnt2 += 1

    if cnt1 > 0:
        return [xor1, xor2]

    return [xor2, xor1]





    