# def countBinarySubstrings(s):

def recurringChar(s):
  d = dict()
  arr = []
  for i in s:
    if i in d:
      d[i] +=1
    else:
      d[i] = 1
  for k,v in enumerate(d):
    if v >= 2:
      arr.append(k)
    return arr[0]
print(recurringChar("ABCBA"))


