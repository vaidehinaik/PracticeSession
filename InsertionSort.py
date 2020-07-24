def insertionSort(arr):
    for i in range(1,len(arr)):
        for j in range(0,i):
            if arr[j] > arr[i]:
                arr[j],arr[i] = arr[i],arr[j]

    return arr
print(insertionSort([3,2,5,1,6]))



[2,3,5,1,6]
[2,3,5,1,6]
i = 3
j = 0,1,2
[1,2,3,5,6]

