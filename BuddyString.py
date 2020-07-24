
def buddyString(s1,s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return False
    res = list()
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            res.append(i)
        if res > 2:
            return False
    if len(res) == 2:
        new_list = list(s2)
        new_list[res[0]], new_list[res[1]] = new_list[res[1]], new_list[res[0]]
        return ''.join(new_list) == s1
    return False
print(buddyString("aaabc","aaacb"))

