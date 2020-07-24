def validAnagram(s,t):
  if len(s) != len(t):
    return False
  arr = 256*[0]
  for i in s:
  # o = ord(i)
    arr[ord(i)] += 1
  # print(arr)
  for i in t:
    if arr[ord(i)] == 0:
      return False
    # print("Not an anagram")
    arr[ord(i)] -= 1
  return True
print(validAnagram("anagram","nagaram"))


