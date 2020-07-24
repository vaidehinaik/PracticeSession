def sortArrayByParityII(A):
    odd, even, n = 1, 0, len(A)
    while odd < n and even < n:
        if A[odd] % 2 == 0 and A[even] % 2 != 0:
            A[odd], A[even] = A[even], A[odd]
        if A[odd] % 2 == 1: odd += 2
        if A[even] % 2 == 0: even += 2
    return A
print(sortArrayByParityII([4,2,5,7]))



def sortArrayByParityII(a):
    even = []
    odd = []
    res = []
    for i in a:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    for i in range(len(a)):
        if i %2 == 0:
            res.append((even.pop()))
        else:
            res.append(odd.pop())
    return res
print(sortArrayByParityII([4,2,5,7]))



