def maxConsOnes(arr):
    max_ones = 0
    curr_ones = 0
    for i in arr:
        if i == 1:
            curr_ones += 1
        elif i == 0:
            if curr_ones != 0 and curr_ones > max_ones:
                max_ones = curr_ones
            curr_ones = 0

    if curr_ones != 0 and curr_ones > max_ones:
        max_ones = curr_ones
        curr_ones = 0
    return max_ones
print(maxConsOnes([1,1,0,1,1,1,1,1,1,1,0,0,1,1,1]))
print(maxConsOnes([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
print(maxConsOnes([0,0,0,0,0,0,0,0,0,0]))



