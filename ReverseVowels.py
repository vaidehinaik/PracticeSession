def reverseVowels(s):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    left = 0
    right = len(s)-1
    str_list = list(s)
    print(str_list)
    while right >= left:
        # print("hello")
        if str_list[left] in vowels and str_list[right] in vowels:
            str_list[left],str_list[right] = str_list[right],str_list[left]

            left += 1
            right -=1
        elif str_list[left] in vowels and str_list[right] not in vowels:
            right -= 1
        elif str_list[left] not in vowels and str_list[right] in vowels:
            left += 1
        else:
            left += 1
            right -=1
        print("i={} j={}".format(left,right))
    return ''.join(str_list)
print(reverseVowels("leetcode"))



