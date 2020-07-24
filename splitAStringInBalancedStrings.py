def splitAStringInBalStrings(s):
    total_substring_bal = 0
    x = 0
    for i in s:
        if i == "R":
            x += 1
        elif i == "L":
            x -= 1
        if x == 0:
            total_substring_bal += 1
    return total_substring_bal
print(splitAStringInBalStrings("RLRRLLRLRL"))


def splitStrInBalStr(s):
    total_bal_substr = 0
    x = 0
    for i in s:
        if i == "R":
            x += 1
        elif i == "L":
            x -= 1
        if x == 0:
            total_bal_substr += 1
    return total_bal_substr
print(splitStrInBalStr("RLLLLRRRLR"))



