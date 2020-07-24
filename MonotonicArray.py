def monotonicArray(arr):
    if len(arr) == 1:
        return True
    mono_inc = True
    mono_dec = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            mono_inc = False
        if arr[i] < arr[i+1]:
            mono_dec = False
    return mono_inc or mono_dec
print(monotonicArray([1,1,1]))



