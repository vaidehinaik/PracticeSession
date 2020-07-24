def sumOfDigitsInTheMinNum(arr):
    s = 0
    min_arr = min(arr)
    str_min_arr = str(min_arr)
    for i in str_min_arr:
        s += int(i)

    if s%2 != 0:
        return 0
    else:
        return 1
print(sumOfDigitsInTheMinNum([99,77,33,66,55]))


