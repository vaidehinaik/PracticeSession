def isGoatLatin(s):
    s = s.split(" ")
    final_list = []
    for idx,word in enumerate(s):
        first_char =word[0]
        if first_char in ("a","e","i","o","u","A","E","I","O","U"):
             word += "ma"
        else:
            word = word[1:] + first_char + "ma"
        word += (idx+1) * "a"
        final_list.append(word)
    return ' '.join(final_list)
print(isGoatLatin("I speak Goat Latin"))



def goatLatin(s):
  s = s.split(" ")
  print("My string is : {}".format(s))
  arr = []
  for i,word in enumerate(s):
    str1 = ""
    if word[0].lower() in ['a','e','i','o','u']:
      str1+=word + "ma"
    else:
      str1 += word[1:]+word[0]+"ma"
    str1 += "a"*(i+1)
    arr.append(str1)
  return " ".join(arr)
print(goatLatin("I speak Goat Latin"))



