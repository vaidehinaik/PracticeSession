# def reverseWords(s):
#     s = s.split(" ")
#     str = ""
#     for i in s:
#         str += i[::-1] + " "
#     return str[:len(str)-1]
# print(reverseWords("Let's take the leetcode contest"))

# Solution 2
def reverseWords(s):
    print(s)
    arr = s.split(" ")
    return " ".join([i[::-1] for i in arr])
print(reverseWords("Let's take the leet code contest"))

