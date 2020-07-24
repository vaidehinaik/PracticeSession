def disappearedNums(A):
    n, res = len(A), []
    A = set(A)
    for i in range(1, n+1):
        if i not in A:
            res.append(i)
    return res
print(disappearedNums([4,3,2,7,8,2,3,1]))



def disappearedNumInAnArray(A):
    for i in range(len(A)):
        new_index = abs(A[i])-1

        if A[new_index] > 0:
            A[new_index] *= -1
    result = []
    for i in range(1,len(A)+1):
        if A[i-1] > 0:
            result.append(i)
    return result
print(disappearedNumInAnArray([4,3,2,7,8,2,3,1]))


# with extra space

def disappearedNum(A):
    d = dict()
    for i in A:
        d[i] = 1
    res = []
    for i in range(1,len(A)+1):
        if i not in d:
            res.append(i)
    return res
print(disappearedNum([4,3,2,7,8,2,3,1]))
