def searchMatrix(matrix, target):
    right ,left = len(matrix) - 1, 0

    while right >= 0 and left < len(matrix[0]):
        val = matrix[right][left]
        if val == target:
            return True
        elif target < val:
            right -= 1
        else:
            left += 1

    return False
print(searchMatrix([[1, 4,  7, 11, 15],[2, 5,  8, 12, 19],[3, 6,  9, 16, 22],[10, 13, 14, 17, 24],[18, 21, 23, 26, 30]],20))



