def continuousSubarray(arr):
    start = None
    end = None
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            if not start:
                start = i
            end = i+1
    return len(arr[start:end+1])
print(continuousSubarray([2, 6, 4, 8, 10, 9, 15]))


def continuousShortestUnsortedArray(arr):
    start = 0
    end = len(arr)-1
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            start = i
            break
    for j in range(len(arr),0):
        if arr[j] < arr[j-1]:
            end = j
            break
    for k in range(start,0, -1):
        if arr[k] > arr[k+1]:
            # arr[k], arr[k+1] = arr[k+1], arr[k]
            start = k
    for l in range(end+1,len(arr)):
        if arr[l] > arr[l+1]:
            # arr[l], arr[l+1] = arr[l+1], arr[l]
            end = l
    len_subarray = end - start
    return (len_subarray)
print(continuousShortestUnsortedArray([2, 6, 4, 8, 10, 9, 15]))




def findUnsortedSubarray(self, nums):
    if not nums or len(nums) < 2:
        return 0
    s = e = None
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            s = i
            break
    for i in range(len(nums)-1, 0, -1):
        if nums[i] < nums[i-1]:
            e = i
            break
    print("s1 {} , e1 {}".format(s, e))
    if s is None or e is None:
        return 0
    min_v = min(nums[s:e+1])
    max_v = max(nums[s:e+1])
    print("minv {} maxv {}".format(min_v, max_v))
    for i in range(0, s):
        if min_v < nums[i]:
            s = i
            break
    for i in range(len(nums)-1, e, -1):
        if max_v > nums[i]:
            e = i
            break
    print("s {} , e {}".format(s, e))
    return e - s + 1
