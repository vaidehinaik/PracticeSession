def thirdMaxNum(nums):
    m1, m2, m3 = float("-inf"), float("-inf"), float("-inf")
    for m in nums:
        if m > m1:
            m1, m2, m3 = m, m1, m2
        elif m1 > m > m2:
            m2, m3 = m, m2
        elif m2 > m > m3:
            m3 = m
    if m3 == float("-inf"):
        return max(m1,m2)
    return m3
print(thirdMaxNum([10,4,6,12,20,15,30]))



def thirdMaxNum(nums):
    if len(nums) < 3:
        print("invalid input")
        return
    first = nums[0]
    for i in range(1,len(nums)):
        if nums[i] > first:
            first = nums[i]

    second = float("-inf")
    for i in range(0, len(nums)):
        if nums[i] > second and nums[i] < first:
            second = nums[i]

    third = float("-inf")
    for i in range(0, len(nums)):
        if nums[i] > third and nums[i] < second:
            third = nums[i]
    return second
print(thirdMaxNum([10,4]))



