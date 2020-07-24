
# Solution 1

def twoSum(numbers,target):
     left = 0
     right = len(numbers)-1
     while left < right:
         sum = numbers[left] + numbers[right]
         if sum == target:
             return [left+1, right+1]
         elif sum < target:
             left += 1
         else:
             right -= 1
     return -1
print(twoSum([2,7,11,15],9))


# solution 2 using dict

def twoSum(nums,target):
    d = dict()
    for i,num in enumerate(nums):
        # print(num)
        if target-num in d:
            return [d[target-num],i]
        d[num] = i
    return None
print(twoSum([2,7,13,16],9))

