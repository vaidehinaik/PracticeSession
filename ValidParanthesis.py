
def validParanthesis(s):
    para_dict = {'{':'}','[':']','(':')'}
    stack = []
    for bracket in s:
        # if bracket not in (para_dict.keys() + para_dict.values()):
        #     continue

        if bracket in para_dict.keys():
            stack.append(bracket)
        elif bracket in para_dict.values():
            if not stack or bracket != para_dict[stack.pop()]:
                return False
        # else:
        #     raise Exception("Unsupported Character: {}".format(bracket))
    if stack:
        return False
    else:
        return True
print(validParanthesis("(){a}kfd"))
