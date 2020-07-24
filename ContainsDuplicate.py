def containsDuplicate(arr):
    d = dict()
    for i,v in enumerate(arr):
        if v in d:
            d[v] += 1
        else:
            d[v] = 1
    for i,v in d.items():
        if v >= 2:
            return True
    return False
print(containsDuplicate([1,2,2,3]))



