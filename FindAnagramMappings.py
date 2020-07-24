# solution 1 with index function

def anagramMapping(arr1,arr2):
    arr = []
    for i in arr1:
        arr.append(arr2.index(i))
    return arr
print(anagramMapping([12, 28,46, 32, 50],[50, 12,32, 46, 28]))


# solution 2

def anagramMapping(arr1,arr2):
    arr = []
    d = dict()
    for i,v in enumerate(arr2):
        d[v] = i
    #   d[arr2[i]] = i
    for i in range(len(arr1)):
        # print(d[arr1[i]])
        arr.append(d[arr1[i]])
    return arr
print(anagramMapping([12, 28,46, 32, 50],[50, 12,32, 46, 28]))




