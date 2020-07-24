def removeElement(arr, key):
    nextElement = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[nextElement] = arr[i]
            nextElement += 1
    return nextElement
print(removeElement([3, 2, 3, 6, 3, 10, 9, 3],3))


