# def reverseArray(arr,left,right):
#     while right > left:
#         arr[left], arr[right] = arr[right],arr[left]
#
#         left += 1
#         right -= 1
#
# def rotateArray(arr,k):
#     k = k % len(arr)
#     reverseArray(arr,0,len(arr)-1)
#     print("Full array reverse {}".format(arr))
#     reverseArray(arr,0,k-1)
#     print("First half array reverse {}".format(arr))
#     reverseArray(arr,k,len(arr)-1)
#     print("second half array reverse {}".format(arr))

def rotateArray2(arr, k):
    k = k % len(arr)
    while k > 0:
        tmp = arr[0]
        tmp2 = None
        for i in range(len(arr)):
            index = (i + 1) % len(arr)
            tmp2 = arr[index]
            arr[index] = tmp
            tmp = tmp2
            # print("tmp: {} tmp2: {} index: {}".format(tmp,tmp2,i))
            # print(arr)
            # import pdb
            # pdb.set_trace()
        k -= 1
    return arr
rotated_arr = rotateArray2([1,2,3,4,5,6,7],2)
print(rotated_arr)



def rotate(nums, k):
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]

        # nums[:] = a
        return a
print(rotate([1,2,3,4,5,6,7],3))
