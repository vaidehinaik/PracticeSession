def isValid(ribbons,l,k):
    pieces = 0
    for ribbon in ribbons:
        pieces += ribbon//l
    if pieces >= k:
        return True
    else:
        return False

def cut_max_ribbon(ribbons,k):
    left = 1
    right = max(ribbons)
    while left+1 < right:
        mid = (left+right)//2
        if isValid(ribbons,mid,k):
            left = mid
        else:
            right = mid - 1
    if isValid(ribbons,right,k):
        return right
    elif isValid(ribbons,left,k):
        return left
    else:
        return 0
print(cut_max_ribbon([1,2,3,4,9],6))



