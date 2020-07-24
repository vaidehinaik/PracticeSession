def decompressEncodedList(arr):
    nums = []
    for i in range(0,len(arr)-1,2):
        nums += arr[i] * [arr[i+1]]
    return nums
print(decompressEncodedList([1,2,3,4]))





