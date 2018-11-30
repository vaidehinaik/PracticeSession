def isMonotonic(arr):
    t1 = True
    t2 = True
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            t1 = False
        elif arr[i] > arr[i+1]:
            t2 = False
    return  t1 or t2
print(isMonotonic([1,3,2]))


