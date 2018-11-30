def reverseString(s):
    left = 0
    right = len(s)-1
    str_list = list(s)
    # while right > left:
    for i in range(len(s)//2 + len(s)%2):
        temp = str_list[left]
        str_list[left] = str_list[right]
        str_list[right] = temp

        left += 1
        right -= 1
    return ''.join(str_list)
print(reverseString("Vaidehi"))


# Soultion 2
# def reverseString(s):
#     return s[::-1]
# print(reverseString("vaidehi"))

# Soultion 3

# def reverse_string_iteratively(s):
#         length = len(s)
#         result = list(s)
#         for i in range(length / 2):
#             result[length - 1], result[i] = s[length - 1], s[i]
#             length -= 1
#         return ''.join(result)
# print(reverse_string_iteratively("sushant"))
