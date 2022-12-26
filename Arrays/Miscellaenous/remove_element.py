'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''
def removeElement(self, nums: List[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = -1
        else:
            k += 1

    j = len(nums) - 1
    for i in range(k):
        if nums[i] == -1:
            while nums[j] == -1:
                j -= 1

            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
    return k