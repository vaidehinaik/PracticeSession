def longestSubstring(s):
    substring = ''
    max_len = curr_len = 0
    for char in s:
        if char in substring:
            index = substring.index(char)
            substring = substring[index+1:]
            curr_len = len(substring)
        substring += char
        curr_len += 1
        if max_len < curr_len:
            max_len = curr_len
    return max_len
print(longestSubstring("pwwkew"))

