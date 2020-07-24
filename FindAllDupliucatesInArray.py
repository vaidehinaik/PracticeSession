# 442. Find All Duplicates in an Array
def findDuplicates(nums):
    dups = list()
    i = 0
    while i < len(nums):
        j = nums[i]-1
        if nums[j] != nums[i]:
            nums[i],nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i+1:
            dups.append(nums[i])
    return dups
print(findDuplicates([4,3,2,7,8,2,3,1]))
