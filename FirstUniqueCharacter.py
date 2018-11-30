def firstUniqueCharacter(s):
    d = dict()
    arr = list()
    if s == "":
        return -1
    for index,value in enumerate(s):
        if value in d:
            d[value] += 1
        else:
            d[value] = 1
    for i,v in enumerate(s):
        if d[v] == 1:
            arr.append(i)
    return arr[0]
print(firstUniqueCharacter("loveleetcode"))


# l = [0] * 256
# print(l)
# str = "loveleetcodeaaaaaaaaa"
#
# for s in str:
#   l[ord(s)] += 1
# print("********** AFTER FILL ***************")
# print(l)
# for s in str:
#   if l[ord(s)] == 1:
#     print("First Non repeat letter: {}".format(s))
