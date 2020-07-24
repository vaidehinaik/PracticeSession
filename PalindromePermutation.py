def canPermutePalindrome(s):
    if len(s) < 2:
       return True
    count = 0
    d = dict()
    for i,v in enumerate(s):
        d[v] = d.get(v, 0) + 1
    for k in d:
        count += d[k] % 2
        if count > 1:
            return False
    return True
print(canPermutePalindrome("code"))
print(canPermutePalindrome("aab"))
print(canPermutePalindrome("carerac"))


