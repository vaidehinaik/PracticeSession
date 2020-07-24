def findNumsInEvenNumOfDigit(nums):
    count = 0
    for i in range(len(nums)):
        if len(str(nums[i]))%2 == 0:
            count += 1
    return count
print(findNumsInEvenNumOfDigit([555,901,482,1771]))




def findNumInEvenNumOfDigitis(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i]%2 == 0:
            count += 1
    return count
print(findNumInEvenNumOfDigitis([12,13,16,17]))


