import sys
def smallestSubArrayWithGivenSum(arr,s):
    window_sum = 0
    window_start = 0
    min_len = sys.maxsize
    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_sum >= s:
          while window_sum >= s:
            min_len = min(min_len, window_end - window_start+1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_len == sys.maxsize:
        return 0
    return min_len
print(smallestSubArrayWithGivenSum([2, 1, 5, 2, 3, 2],7))



