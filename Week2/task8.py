# 8. Given an integer array nums, move all 0's to the end of it while maintaining the
# relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
def move_zeroes(nums):
    non_zero_index = 0  
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1    
    for i in range(non_zero_index, len(nums)):
        nums[i] = 0    
    return nums