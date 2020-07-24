def selectionSort(arr):
    for i in range(len(arr)):
        i_min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i_min]:
                i_min = j
        arr[i],arr[i_min] = arr[i_min],arr[i]
    return arr
print(selectionSort([5,1,7,2,8,3,9,4]))



