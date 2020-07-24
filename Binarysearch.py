def binarySearch(item_list, item):
    left = 0
    right = len(item_list)-1
    found = False
    while right >= left:
        mid = (left+right)//2
        if item_list[mid] == item:
            return True
        else:
            if item < item_list[mid]:
                right = mid - 1
            else:
                left = mid+1
    return found
print(binarySearch([1,2,5,7,9,11,13,15],7))



def binarySearch(item_list,item):
    left = 0
    right = len(item_list)-1
    while right >= left:
        mid = (left+right)//2
        if item_list[mid] == item:
            return mid
        else:
            if item < item_list[mid]:
                right = mid - 1
            else:
                left = mid+1
    return -1
print(binarySearch([1,3,5,7,9,11,13,15],15))



