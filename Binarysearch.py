# def binarySearch(item_list,target):
#     first = 0
#     last = len(item_list)-1
#     found = False
#     while last >= first and not found:
#         mid = (first+last)//2
#
#         if target == item_list[mid]:
#             return True
#         else:
#             if target > item_list[mid]:
#                 first = mid + 1
#             else:
#                 last = mid - 1
#     return found
# print(binarySearch([1,2,3,4,5,7,8],9))



def binarySearch(item_list,item):
    first = 0
    last =len(item_list)-1
    while first <= last:
        mid = (first+last)//2

        if item == item_list[mid]:
            return mid
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return
print(binarySearch([1,2,3,4,5],3))


