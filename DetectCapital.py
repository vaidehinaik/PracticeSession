def detectCapital(s):
    if ord(s[0]) in range(65,91):
        if ord(s[1]) in range(65,91):
            for i in s[2:]:
                o = ord(i)
                if o not in range(65,91):
                    return False
                # else:
                #     return True
        if ord(s[1]) in range(97,123):
            for i in s[2:]:
                o = ord(i)
                if o not in range(97,123):
                    return False
                # else:
                #     return True
    else:
        if ord(s[0]) in range(97,123):
            for i in s[1:]:
                o = ord(i)
                if o not in range(97,123):
                    return False
    return True
print(detectCapital("Google"))



def detectCapital(s):
    if ord(s[0]) in range(65,91):
        if ord(s[1]) in range(65,91):
            for i in s[2:]:
                o = ord(i)
                if o not in range(65,91):
                    return False
        if ord(s[1]) in range(97,123):
            for i in s[2:]:
                o = ord(i)
                if o not in range(97,123):
                    return False
    else:
        if ord(s[0]) in range(97,123):
            for i in s[1:]:
                o = ord(i)
                if o not in range(97,123):
                    return False
    return True
print(detectCapital("India"))



def detectCapital(s):
    if ord(s[0]) in range(65,91):
        if ord(s[1]) in range(65,91):
            for i in s[2:]:
                o = ord(i)
                if o not in range(65,91):
                    return False
        if ord(s[1]) in range(97,123):
            for i in s[2:]:
                o = ord(i)
                if o not in range(97,123):
                    return False
    else:
        if ord(s[0]) in range(97,123):
            for i in s[1:]:
                o = ord(i)
                if o not in range(97,123):
                    return False
    return True
print(detectCapital("Vaidehi"))








