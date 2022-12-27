'''
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, 
where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly. 
That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
'''
def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
    ans = []
    for i in range(len(nums)):
        left = lower
        right = nums[i] - 1
        if left < right:
            ans.append(str(left) + "->" + str(right))

        if left == right:
            ans.append(str(left))

        lower = nums[i] + 1

    left = lower
    right = upper
    if left < right:
        ans.append(str(left) + "->" + str(right))

    if left == right:
        ans.append(str(left))

    return ans