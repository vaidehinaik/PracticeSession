# def jewelsAndStones(j,s):
#     count = 0
#     for i in s:
#         if i in j:
#             count += 1
#     return count
import re
def jewelsAndStones(j, s):
    count = 0
    for i in j:
        # count += s.count(i)
        count += len(re.findall(i, s))
    return count

print(jewelsAndStones("aAab","aaAbbb"))



def jewelsAndStone(j,s):
    count = 0
    for i in s:
        if i in j:
            count += 1
    return count
print(jewelsAndStones("aAab","aaAbbb"))

