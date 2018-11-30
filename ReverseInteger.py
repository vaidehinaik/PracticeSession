def reverseInteger(num):
    s = ""
    multiplier = 1
    if num < 0:
        multiplier = -1
    num = abs(num)
    while num != 0:
        rem = num % 10
        s += str(rem)
        num = num//10
    s = s.lstrip("0")
    return int(s) * multiplier
print(reverseInteger(-123))

