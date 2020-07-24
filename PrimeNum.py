def primeNum(lower,upper):
    arr = list()
    for num in range(lower,upper+1):
        if num >1:
            for i in range(2,num//2+1):
                if num%i == 0:
                    break
            else:
                arr.append(num)
    return arr
print(primeNum(2,19))



