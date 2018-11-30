def isValidPalindrome(s):
    left = 0
    right = len(s)-1
    while right >= left:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True
print(isValidPalindrome("A man, a plan, a canal: Panama"))
