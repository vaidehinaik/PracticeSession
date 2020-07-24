# 973. K Closest Points to Origin

def closestPointToOrigin(points, K):
    def sortlist(x):
        return (x[0]**2 + x[1]**2)
    points.sort(key = sortlist)
    return points[:K]
print(closestPointToOrigin([[1,3],[-2,2]],1))


