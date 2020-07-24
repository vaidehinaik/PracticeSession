# def houseRobber(nums):
#     if not nums:
#             return 0
#     n = len(nums)
#     if n < 2:
#         return nums[0]
#     dp = [-1]*n
#     print(dp)
#     dp[0] = nums[0]
#     dp[1] = max(nums[0],nums[1])
#     # dp[2] = max(nums[0]+nums[2], nums[1])
#     for i in range(2,len(nums)):
#         dp[i] = max(dp[i-1],dp[i-2]+nums[i])
#     return dp[-1]
# print(houseRobber([1,2,3,1]))



def slowestKey(keyTimes):
    keyTimes = [[chr(k[0] + 97), k[1]] for k in keyTimes]
    print("key times: {}".format(keyTimes))
    longest_key = None
    longest_duration = None
    for i in range(len(keyTimes)-1):
        if i == 0:
            start = 0
        else:
            start = keyTimes[i-1][1]
        end = keyTimes[i][1]
        char = keyTimes[i][0]
        interval = end - start
        if not longest_duration or interval > longest_duration:
            longest_duration = interval
            longest_key = char
        return longest_key
print(slowestKey([[0, 2], [1, 5], [0, 9], [2, 15]]))
