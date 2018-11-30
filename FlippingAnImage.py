def flippingAnImage(arr):
    final_list = []
    for i in arr:
        temp_list = []
        for j in i[::-1]:
            if j == 0:
                temp_list.append(1)
            else:
                temp_list.append(0)
        final_list.append(temp_list)
    return final_list
print(flippingAnImage([[1,1,0],[0,0,0],[1,0,1]]))

