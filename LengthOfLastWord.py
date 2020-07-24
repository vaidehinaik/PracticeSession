# def lengthOfLastWord(s):
#     str_new = s.split(" ")
#     if len(str_new) == 0:
#         return 0
#     elif len(str_new) == 1:
#         return len(str_new[0])
#     else:
#         return len(str_new[-1])
# print("The length of the last word is :{}".format(lengthOfLastWord("My name is aaaaaaa")))


def lengthOfLastWord(s):
    str_new = s.split(" ")
    # str_new = str_new[::-1]
    if len(str_new) == 0:
        return 0
    return len(str_new[-1])
print("The length of the last word is: {}".format(lengthOfLastWord("My name is bbbbbbbbbbbbbb")))
