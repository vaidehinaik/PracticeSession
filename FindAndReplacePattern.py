def findAndReplacePattern(words,pattern):
    pattern_idx = ''
    res = []
    for i in pattern:
        pattern_idx += str(pattern.index(i))
    for i in words:
        temp_idx = ''
        for j in i:
            temp_idx += str(i.index(j))
            if temp_idx == pattern_idx:
                res.append(i)
    return res
print(findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"],"abb"))




