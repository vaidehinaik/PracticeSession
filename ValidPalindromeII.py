# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

def isPalindromeII(s):
    left = 0
    right = len(s)-1
    while right >= left:
        if s[left] == s[right]:
            return True
        else:
            left += 1
            right -=1


