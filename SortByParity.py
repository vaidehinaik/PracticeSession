# Solution 1
def sortArrayByParity(arr):
  left = 0
  right = len(arr)-1
  while right > left:
    if arr[left]%2 != 0 and arr[right]%2 == 0:
      arr[left],arr[right] = arr[right],arr[left]
    elif arr[left]%2 == 0 and arr[right]%2 == 0:
      left += 1
    elif arr[left]%2 != 0 and arr[right]%2 != 0:
      right -= 1
    else:
      left += 1
      right -=1
  return arr
print(sortArrayByParity([3,1,2,4]))


# Solution using list comprehension

def sortArrayByParity(A):
  return [i for i in A if i%2 == 0] + [i for i in A if not i%2 == 0]
print(sortArrayByParity([3,1,2,4]))



