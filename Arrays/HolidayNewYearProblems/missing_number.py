'''
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
'''
def missingNumber(self, nums: List[int]) -> int:
    sum1 = 0
    for i in nums:
        sum1 += i
    
    return (len(nums) * (len(nums) + 1)) // 2 - sum1