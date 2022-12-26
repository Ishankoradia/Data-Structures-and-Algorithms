'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''
def searchInsert(self, nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1
    while start <= end:
        middle = (end + start) // 2
        if target > nums[middle]:
            start = middle + 1
        elif target < nums[middle]:
            end = middle - 1
        else:
            return middle

    if end < 0:
        return 0

    if start > len(nums) - 1:
        return start

    return start