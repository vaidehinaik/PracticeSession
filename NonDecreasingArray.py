
def isNonDecreasing(nums):
# Return True for Array length <=2
    if len(nums) <=2:
        return True
    # Iterate over the array and count any invalid pattern cases
    count = 0
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            count +=1
            if count >1:
                return False # Cannot convert for invalid pattern >=2
            if i>0:
                # Considering 1st scenario that we need modify i+1 entry.
                if nums[i-1] >nums[i+1]:
                    nums[i+1] = nums[i]
                # Below is the other scenario to change i entry, No need to implement
                #else:
                #   nums[i] = nums[i-1]
    return True

# print(isNonDecreasing([1,4,2,3]))
print(isNonDecreasing([3,4,2,3]))


