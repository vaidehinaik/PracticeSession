def continuousSubarray(arr):
    start = None
    end = None
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            if not start:
                start = i
            end = i+1
    return len(arr[start:end+1])
print(continuousSubarray([2, 6, 4, 8, 10, 9, 15]))


