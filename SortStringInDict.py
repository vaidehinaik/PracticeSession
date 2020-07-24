def compare(a, b):
  l1 = len(a)
  l2 = len(b)
  # print("*****")
  # print(">>> len1 {} : {}".format(a, len(a)))
  # print(">>> len2 {} : {}".format(b, len(b)))
  l_range = [i for i in range(97, 123)]
  u_range = [i for i in range(65, 91)]
  if l1 > l2:
    # print("len greater")
    # print("*****")
    return True
  if a.lower() == b.lower():
    # print("string equals")
    # print("*****")
    if ord(a[0]) in u_range and ord(b[0]) in l_range:
      return True
    if ord(a[0]) in u_range and ord(b[0]) in u_range:
      if len(a) > 1 and ord(a[1]) in u_range and ord(b[1]) in l_range:
        return True
  else:
    # print("arrange as per dictionary")
    # print("*****")
    for i in range(len(a)):
      if ord(a[i].lower()) > ord(b[i].lower()):
        return True
  return False

def sort_dictionary(arr):
  for i in range(len(arr)):
    for j in range(0, len(arr) - 1 - i):
      if compare(arr[j], arr[j+1]):
        # print("arr[j]: {} arr[j+1]: {}".format(arr[j], arr[j+1]))
        tmp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = tmp
  return arr

arr = ["Abc", "a", "ab", "xyz", "BCD", "#$%bcd", "A", "bcd", "A"]
to_be_sorted = []
for i, word in enumerate(arr):
  isValid = True
  for c in word:
    if not c.isalpha():
      isValid = False
      break
  if isValid:
    to_be_sorted.append(word)
print("INPUT ARR: {}".format(arr))
print("TO BE SORTED: {}".format(to_be_sorted))
print("SORTED: {}".format(sort_dictionary(to_be_sorted)))
