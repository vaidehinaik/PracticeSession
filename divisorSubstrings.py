def substringDivisor(num,k):
    output = set()
    divisors = set()
    num = str(num)

    for i in range(len(num)):
        if len(num[i:i+k]) == k:
            divisors.add(int(num[i:i+k]))

    for i in divisors:
        if int(num)%i == 0:
            output.add(i)
    return len(output)
print(substringDivisor(555,1))

