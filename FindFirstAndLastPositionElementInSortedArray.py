def findFirstAndlastElement(nums, target):
    left = 0
    right = len(nums)-1
    while right >= left:
        if nums[left] == target and nums[right] == target:
            return [left, right]
        elif nums[left] == target and nums[right] != target:
            right -= 1
        elif nums[left] != target and nums[right] == target:
            left += 1
        else:
            left += 1
            right -= 1
    return [-1, -1]
print(findFirstAndlastElement([5,7,7,8,8,10], 6))



def findFirstLastElementIndex(nums, target):
    start = 0
    end = len(nums)-1
    while end >= start:
        mid = (start+end)//2
        if nums[mid] < target:
            start = mid+1
        elif nums[mid] > target:
            end = mid - 1
        else:
            if nums[start] == target and nums[end] == target:
                return [start, end]
            if nums[start] < target:
                start += 1
            if nums[end] > target:
                end -= 1
    return [-1,-1]
print(findFirstLastElementIndex([5,7,7,8,8,10], 6))



