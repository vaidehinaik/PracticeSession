
# https://leetcode.com/discuss/interview-question/439106/Postmates-or-OA-2019-or-Good-Tuples/395286
def goodTuple(arr):
    expected_uni_len = 2
    good_tup = list()

    for i in range(len(arr)):
        if len(arr[i:i+3]) == 3 and len(set(arr[i:i+3])) == expected_uni_len:
            good_tup.append(arr[i:i+3])
    print(good_tup)
    return len(good_tup)
print(goodTuple([4,4,6,1,2,2,2,3]))
