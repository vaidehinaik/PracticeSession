def judgeCircle(moves):
    if moves == 0:
        return True
    i = 0
    j = 0
    for move in moves:
        if move == "U":
            i += 1
        elif move == "D":
            i -= 1
        elif move == "R":
            j += 1
        elif move == "L":
            j -= 1
        else:
            return "Invalid Moves"
    if i == 0 and j == 0:
        return True
    else:
        return False
print(judgeCircle("12334"))


def judgeCircle(moves):
    return moves.count("R") == moves.count("L") and moves.count("U") == moves.count("D")
print(judgeCircle("UD"))



