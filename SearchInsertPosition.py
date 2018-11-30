def searchInsertPosition(arr,target):
    # print(arr[-1])
    if target < arr[0]:
        return 0
    if target > arr[-1]:
        return len(arr)
    for i,v in enumerate(arr):
        if v == target:
            return i
        else:
            if target > arr[i] and target < arr[i+1]:
                return i+1
print(searchInsertPosition([1,3,5,6,7],8))



