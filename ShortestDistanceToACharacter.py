def shortestDisToAChar(S,C):
    prev = float("-inf")
    ans = []
    for i,v in enumerate(S):
        if v == C:
            prev = i
        ans.append(i-prev)

    prev = float("inf")
    for i in range(len(S)-1,-1,-1):
        if S[i] == C:
            prev = i
        ans[i] = min(ans[i], prev-i)
    return ans
print(shortestDisToAChar("loveleetcode",'e'))

