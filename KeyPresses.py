def arraykeyPresses(s1, s2):
    print("s1: {}".format(s1))
    print("s2: {}".format(s2))
    stack1 = []
    stack2 = []
    if (s1 is None):
        return stack1
    for i in range(len(s1)):
        if s1[i] != 'b':
            stack1.append(s1[i])
        else:
            stack1.pop();
            # i += 1
        i += 1
    # print("Stack1: {}".format(stack1))
    # print("Stack2: {}".format(stack2))
    if (s2 is None):
        return stack2
    for i in range(len(s2)):
        if s2[i] != 'b':
            stack2.append(s2[i])
        else:
            stack2.pop();
        i += 1
    if stack1 != stack2:
        print("Stack1: {}".format(stack1))
        print("Stack2: {}".format(stack2))
        return False
    else:
        return True
print(arraykeyPresses("ABC\\b\\b\\bABC","ABCABC\\b\\b\\b"))


