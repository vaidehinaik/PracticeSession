def palindrome_Num(x):
    if x < 0 :
        return False
    beg = x
    rev = 0
    while x > 0:
        rev = rev*10 + x%10
        x = x//10
    return beg == rev
print(palindrome_Num(-1))


