def twoSum(nums,target):
    d = dict()
    for i,num in enumerate(nums):
        if target-num in d:
            return [d[target-num],i]
        d[num] = i
    return nums
print(twoSum([15,11,7,2],9))



