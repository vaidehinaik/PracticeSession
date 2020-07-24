def removeVowels(s):
    if s == "aeiou":
        return " "
    left = 0
    right = len(s)-1
    arr = []
    while right >= left:
        if s[left] == "a" or s[left] == "e" or s[left] == "i" or s[left] == "o" or s[left] == "u":
            left += 1
        else:
            arr.append(s[left])
            left += 1
    return ''.join(arr)
print(removeVowels("aeiou"))



