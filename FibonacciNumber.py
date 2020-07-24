def fibonacciNumber(N):
    prev = 0
    curr = 1
    if N == 0:
        return prev
    elif N == 1:
        return curr
    else:
        for i in range(N-1):
            prev, curr = curr, curr+prev
    return curr
print(fibonacciNumber(4))


