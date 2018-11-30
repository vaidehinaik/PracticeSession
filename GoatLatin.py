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



