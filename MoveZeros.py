def moveZeros(nums):
    zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i],nums[zero] = nums[zero],nums[i]

            zero += 1
        print("zeroIndex: {} , index: {}, nums: {}".format(zero,i,nums))
    return nums
# print(moveZeros([0,1,0,2,8,10]))
# print(moveZeros([0,1,2,3,4,5,0]))

print(moveZeros([1,2,0,1,0,0]))



