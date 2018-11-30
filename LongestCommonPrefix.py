def longestCommonPrefix(words):
    res = ""
    min_word = min(words, key = len)
    for index,letter in enumerate(min_word):
        for word in words:
            if word[index] != letter:
                return res
        res += letter
    return res
print(longestCommonPrefix(["flower","flow","flight"]))


