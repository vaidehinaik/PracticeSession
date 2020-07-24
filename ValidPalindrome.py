def isPalindrome(s):
    if type(s) is not str:
        return False
    if s is None or s == '' or len(s) == 1:
        return True
    start = 0
    end = len(s)-1
    while end >= start:
        if not s[start].isalpha():
            start += 1
            continue
        if not s[end].isalpha():
            end -= 1
            continue
        if s[start].lower() != s[end].lower():
            return False
        else:
            start += 1
            end -= 1
    return True
print(isPalindrome("A man, a plan, a canal: Panama"))



