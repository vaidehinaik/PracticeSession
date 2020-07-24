

def maxSubArray(nums):
    max_end = nums[0]
    max_so_far = nums[0]
    for num in nums[1:]:
        max_so_far = max(max_so_far+num, num)
        max_end = max(max_end, max_so_far)
    return max_end
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
