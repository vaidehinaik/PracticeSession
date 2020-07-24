def parseExpression(s):
    stack = []
    for i in s:
        if i is not ")":
            stack.append(i)
        j = stack.pop()
        while j is not "(":

