def linearSearch(arr_list,target):
    pos = 0
    found = False
    while pos < len(arr_list) and not found:
        if arr_list[pos] == target:
            found = True
        else:
            pos += 1
    # if found == False:
    #     print("Target is not in the list")
    return found,pos
print(linearSearch([11,23,58,31,56,77,43,12,65,19],31))

def linearSearch(arr_list,target):
    for i in range(len(arr_list)):
        if arr_list[i] == target:
            return i
    return -1
print(linearSearch([11,23,58,31,56,77,43,12,65,19],30))

