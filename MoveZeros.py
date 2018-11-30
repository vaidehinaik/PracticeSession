def moveZeros(nums):
    zero = 0
    for num in range(len(nums)):
        if nums[num] != 0:
            nums[num],nums[zero] = nums[zero],nums[num]

            zero += 1
    return nums
print(moveZeros([0,1,0,2,8,10]))



