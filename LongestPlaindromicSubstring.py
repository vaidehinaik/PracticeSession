def longestPalindromicSubstring(s):
    if len(s) == 0:
        return s
    for i in range(len(s), 0, -1):
        for j in range(0, len(s)-i+1):
            if s[j:j+i] == s[j:j+i][::-1]:
                return s[j:j+i]
print(longestPalindromicSubstring("baabbaad"))



