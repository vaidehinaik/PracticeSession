 def lowerCase(s):
    str = ""
    for i in s:
        o = ord(i)
        if o >= 65 and o <= 90:
            str += chr(o+32)
        else:
            str += i
    return str
print(lowerCase("VAIDEHI"))
