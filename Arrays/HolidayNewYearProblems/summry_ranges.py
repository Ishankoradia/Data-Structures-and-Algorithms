'''
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, 
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
'''
def summaryRanges(self, nums: List[int]) -> List[str]:
    ans = []
    c = 0
    left = None
    right = None
    while c < len(nums):
        if c == 0:
            left = nums[c]
            right = nums[c]

        if c > 0:
            if nums[c] == right + 1:
                right = nums[c]
            else:
                if left == right:
                    ans.append(str(left))
                else:
                    ans.append(str(left) + '->' + str(right))

                left = nums[c]
                right = nums[c]

        c += 1

    if left is not None and right is not None:
        if left == right:
            ans.append(str(left))
        else:
            ans.append(str(left) + '->' + str(right))

    return ans
