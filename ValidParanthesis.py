class ValidParanthesis:
    def isValid(self,s):
        stack = []
        dict = {"{":"}","[":"]","(":")"}
        for bracket in s:
            if bracket in dict.keys():
                stack.append(bracket)

            elif bracket in dict.values():
                # if not stack:
                #     return False
                if not stack or bracket != dict[stack.pop()]:
                    return False
            else:
                raise Exception("Unsupported type: {}".format(bracket))
        return True

if __name__ == "__main__":
    vp = ValidParanthesis()
    print(vp.isValid("{[()]}"))
    print(vp.isValid(")}[)]("))



def validParanthesis(s):
    stack= []
    d = {"{":"}","[":"]","(":")"}
    for bracket in s:
        if bracket in d.keys():
            stack.append(bracket)
        elif bracket in d.values():
            if not stack or bracket != d[stack.pop()]:
                return False
        else:
            raise Exception("unsupported character: {}".format(bracket))
    if stack:
        return False
    return True
print(validParanthesis("{[]}"))

