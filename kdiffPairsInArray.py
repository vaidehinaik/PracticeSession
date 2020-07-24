def kdiffPairs(arr,k):
    d = dict()
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            # print("a[j]: {}".format(arr[j]))
            if abs(arr[i] - arr[j]) == k:
                # print(abs(arr[i] - arr[j]))
                # print(arr[i])
                # print(arr[j])
                if arr[i] > arr[j]:
                    d[arr[i]] = arr[j]
                else:
                    d[arr[j]] = arr[i]
    return len(d.items())
print(kdiffPairs([1, 3, 1, 5, 4],0))


# a = [3, 1, 4, 1, 5]
# arr = list()
# diff = 2
# for i in range(0, len(a)-1):
#   for j in range(i+1, len(a)):
#     if abs(a[i] - a[j]) == diff:
#       if (a[i], a[j]) not in arr and (a[j], a[i]) not in arr:
#         arr.append((a[i], a[j]))
# print(arr)


a = [1,2,3,4,5,6,7]
k = 3
# # Step 1
# diff = len(a) - k #4
# a1 = a[0:4]
# a2 = a[4:]
# print(a2 + a1)
#
# def reverse(arr):
#   left = 0
#   right = len(arr)-1
#   while right >= left:
#     arr[left],arr[right] = arr[right],arr[left]
#     left += 1
#     right -= 1
#   return arr
#
# rev = reverse(a)
# print(rev)
# rev = reverse(rev[:3]) + reverse(rev[3:])
# print(rev)
# # print(rev)
