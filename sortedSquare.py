# # 977. Squares of a Sorted Array
# # Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
# #
# #
# #
# # Example 1:
# #
# # Input: [-4,-1,0,3,10]
# # Output: [0,1,9,16,100]
# # Example 2:
# #
# # Input: [-7,-3,2,3,11]
# # Output: [4,9,9,49,121]
# #
# # Input:
# A = [-4,-1,0,3,10]
# A = [-7,-3,2,3,11]
#
# # *Algorithm: O(n) time and space
# # 1. Take two pointers i, j starting at 0 and len(A) - 1 respectively
# # 2. While i <= j, run the operations of calculating the max square
# # 3. Add whichever gives max square result to the array first and move its corresponding pointer
# # 4. Finally return the reverse of the result list
# # def sortedSquaresTWO_POINTERS(A):
# #     i = 0; j = len(A) - 1; result = []
# #     while(i <= j):
# #         if abs(A[i]) > abs(A[j]): result.append(A[i] ** 2); i += 1
# #         else: result.append(A[j] ** 2); j -= 1
# #     return result[::-1]
# #
# # print(sortedSquaresTWO_POINTERS(A))
# # # Algorithm: O(nlogn) time and O(n) space (Naive Solution)
# # # 1. Find squares
# # # 2. Sort the Array (sort() is faster than sorted() for lists)
# # def sortedSquares(A):
# #     A = [x ** 2 for x in A]
# #     result = A.sort()
# #     return result
# #
# # print(sortedSquares(A))
# #
# #
# #
def sortedSquare(a):
  left = 0
  right = len(a)-1
  res = []
  while right >= left:
    if abs(a[left]) > abs(a[right]):
      res.append(a[left]**2)
      left += 1
    else:
      res.append(a[right]**2)
      right -= 1
  return res[::-1]
print(sortedSquare([-4,-1,0,3,10]))

