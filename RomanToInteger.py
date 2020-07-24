def romanToInteger(s):
    d = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD":400,
    "CM":900
    }


    ans = 0
    skip_next_itr = False
    for i in range(len(s)):
        if skip_next_itr:
            skip_next_itr = False
            continue
        if i == len(s)-1:
            ans += d[s[i]]
        elif s[i] in d.keys():
            if s[i:i+2] in d.keys():
                ans += d[s[i:i+2]]
                skip_next_itr = True
            else:
                ans += d[s[i]]
    return ans
print(romanToInteger("LVIII"))


def romanToInteger(s):
    d = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD":400,
        "CM":900
    }
    ans = 0
    skip_next_itr = False
    for i in range(len(s)):
        if skip_next_itr:
            skip_next_itr = False
            continue
        if i == len(s)-1:
            ans += d[s[i]]
        elif s[i] in d.keys():
            if s[i:i+2] in d.keys():
                ans += d[s[i:i+2]]
            else:
                ans += d[s[i]]
    return ans
print(romanToInteger("LVIII"))
