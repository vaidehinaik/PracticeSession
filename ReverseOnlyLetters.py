def reverseOnlyLetters(s):
    left = 0
    right = len(s)-1
    str_list = list(s)
    while right >= left:
        if str_list[left].isalpha() and str_list[right].isalpha():
            str_list[left], str_list[right] = str_list[right],str_list[left]
            left += 1
            right -= 1
        else:
            if not str_list[left].isalpha():
                left += 1
            if not str_list[right].isalpha():
                right -= 1
    return "".join(str_list)
print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))
