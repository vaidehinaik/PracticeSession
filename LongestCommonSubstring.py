def longestCommonSubstring(s1,s2):
    if s1 == None or len(s1) == 0 or s2 == None or len(s2) == 0:
        return " "
    len1 = len(s1)
    len2 = len(s2)
    max = 0
    res = ""
    for i in s1:
        for j in s2:
            start1 = i
            start2 = j
            curr = 0
            while start1 < len1 and start2 < len2:
                c1 = s1[start1]
                c2 = s2[start2]

                if c1 == c2:
                    start1 += 1
                    start2 += 1
                    curr += 1
                else:
                    if curr > max:
                        max = curr

                        end = start1 - 1
                        res = s1.Substring(i, end - i +1)
                    break
    return res

print(longestCommonSubstring("thisisabrowndog","mydogscolorisbrown"))

