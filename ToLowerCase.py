def toLowerCase(s):
    ret = ""
    for i in s:
        o = ord(i)
        if o >= 65 and o <= 90:
            ret += chr(o+32)
        else:
            ret += i
    return ret
print(toLowerCase("SUSHANT"))

