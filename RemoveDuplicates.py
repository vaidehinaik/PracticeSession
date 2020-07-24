def removeDuplicates(arr):
    nextNonDuplicate = 1
    i = 1
    while i < len(arr):
        if arr[nextNonDuplicate - 1] != arr[i]:
            arr[nextNonDuplicate] = arr[i]
            nextNonDuplicate += 1
        i += 1
    return nextNonDuplicate
print(removeDuplicates([2, 3, 3, 3, 6, 9, 9]))



