def findAverageOfSubArrays(arr,k):
    result = []
    window_sum = 0.0
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k-1:
            result.append(window_sum/k)
            window_sum -= arr[window_start]
            window_start += 1
    return result
print(findAverageOfSubArrays([1, 3, 2, 6, -1, 4, 1, 8, 2],5))



