def three_Sum(nums):
    d = dict()
    nums = sorted(nums)
    for i in range(len(nums)):
        j,k = 0, len(nums)-1
        while j < i < k:
            vals = (nums[j], nums[i], nums[k])
            s = sum(vals)
            if s == 0:
                d[vals] = True
            if  s < 0:
                j += 1
            else:
                k -= 1
    return d.keys()
print(three_Sum([-1, 0, 1, 2, -1, -4]))



