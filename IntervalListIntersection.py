def listIntersection(A, B):
    ans = []
    i = j = 0
    while i < len(A) and j < len(B):
        lo = max(A[i][0], B[j][0])
        hi = min(A[i][1], B[j][1])

        if lo <= hi:
            ans.append([lo,hi])

        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return ans
print(listIntersection([[0,2],[5,10],[13,23],[24,25]],[[1,5],[8,12],[15,24],[25,26]]))


