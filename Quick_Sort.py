def quick_sort(data_list):
    quick_sort_helper_func(data_list,0, len(data_list)-1)

def quick_sort_helper_func(data_list, first, last):
    if last > first:
        split_pnt = partition(data_list, first, last)
        quick_sort_helper_func(data_list, first, split_pnt-1)
        quick_sort_helper_func(data_list, split_pnt+1, last)

def partition(data_list,first,last):
    pivot_val = data_list[last]
    left = first
    right = last - 1

    flag = False

    while not flag:
        while left <= right and data_list[left] < pivot_val:
            left += 1
        while left <= right and data_list[right] > pivot_val:
            right -= 1

        if left > right:
            flag = True

        else:
            data_list[left],data_list[right] = data_list[right],data_list[left]

    data_list[left], pivot_val = pivot_val, data_list[left]
    return left
print(quick_sort([10,1,9,2,8,3,7,4,6,5]))



