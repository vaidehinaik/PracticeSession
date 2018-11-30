# Solution 1 using extra space
#
def singleNumber(arr):
    d = dict()
    for a in arr:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    for k,v in d.items():
        if v == 1:
            return k;
print(singleNumber([1,1,2,2,3,3,4]))


# Solution 2 using xoring

def singleNumber(nums):
    ans = 0
    for num in nums:
        ans = ans ^ num
        # print(ans)
    return ans
print(singleNumber([1,2,2,3,3,1,10]))
