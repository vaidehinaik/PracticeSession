# Given an array A of distinct integers sorted in ascending order, return the smallest index i that satisfies A[i] == i.  Return -1 if no such i exists.
#
# Example 1:
#
# Input: [-10,-5,0,3,7]
# Output: 3
# Explanation:
# For the given array, A[0] = -10, A[1] = -5, A[2] = 0, A[3] = 3, thus the output is 3.
# Example 2:
#
# Input: [0,2,5,8,17]
# Output: 0
# Explanation:
# A[0] = 0, thus the output is 0.
# Example 3:
#
# Input: [-10,-5,3,4,7,9]
# Output: -1
# Explanation:
# There is no such i that A[i] = i, thus the output is -1.

# itervative method
def fixed_point(A):
    arr = []
    for i in range(len(A)):
        if A[i] == i:
            arr.append(i)
    if not arr:
        return -1
    else:
        return arr[0]
print(fixed_point([0,2,5,8,17]))


# binary search method

def fixedPoint(A):
    left = 0
    right = len(A)-1
    while right >= left:
        mid = (left+right)//2
        if mid == A[mid]:
            return mid
        else:
            if mid < A[mid]:
                right -= 1
            else:
                left += 1
    return -1
print(fixedPoint([-10,-5,0,3,7]))

