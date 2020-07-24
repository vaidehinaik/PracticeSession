def searchInARotatedSortedArray(nums, target):
    first = 0
    last = len(nums)-1
    while last >= first:
        mid = (first+last)//2
        if nums[mid] == target:
            return mid

        if nums[mid] < nums[last]:
            if nums[mid] < target <= nums[last]:
                first = mid + 1
            else:
                last = mid - 1
        else:
            if nums[first] <= target < nums[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return -1
print(searchInARotatedSortedArray([4,5,6,7,0,1,2],3))


