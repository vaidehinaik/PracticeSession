
# Solution 1
def judgeCircle(moves):
    if not moves:
        return True
    i = 0
    j = 0
    for move in moves:
        if move == "R":
            i += 1
        elif move == "L":
            i -= 1
        elif move == "U":
            j += 1
        elif move == "D":
            j -= 1
        else:
            print("Invalid moves")
    if i == 0 and j == 0:
        return True
    else:
        return False
print(judgeCircle("LL"))

# Soultion 2
# def judgeCircle(moves):
#     return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")
# print(judgeCircle("LR"))


# Soultion 3
# def judgeCircle(moves):
#         """
#         :type moves: str
#         :rtype: bool
#         """
#
#         d = {'L': 0, 'R': 0, 'U':0, 'D':0}
#         for i in moves:
#             d[i] += 1
#
#         return d['L'] == d['R'] and d['U'] == d['D']
# print(judgeCircle("LR"))

