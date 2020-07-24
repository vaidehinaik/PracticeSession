def transposeMatrix(A):
    R = len(A)
    C = len(A[0])
    result = [[None] * R for _ in range(C)]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[j][i] = A[i][j]
    return result

print(transposeMatrix([[1,2,3,10],[4,5,6,11],[7,8,9,12],[13,14,15,16]]))


