def majorityElement(arr):
    d = dict()
    for maj_ele in arr:
        if maj_ele in d:
            d[maj_ele] += 1
        else:
            d[maj_ele] = 1
    # for v in arr:
        if d[maj_ele] > len(arr)//2:
            return maj_ele
print(majorityElement([2,2,1,1,1,2,10,10,10,10,10,10,10,10]))



