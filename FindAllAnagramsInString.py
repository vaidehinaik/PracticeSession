# GOOD SOLUTION - sliding window
from collections import Counter
def findAnagrams(s, p):
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)
        s_count = Counter()

        output = []
        # sliding window on the string s
        for i in range(ns):
            # add one more letter
            # on the right side of the window
            s_count[s[i]] += 1
            # remove one letter
            # from the left side of the window
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1
            # compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                output.append(i - np + 1)

        return output

def isAnagram(s,t):
    if len(s) != len(t):
        return False
    arr = 256*[0]
    for i in s:
        arr[ord(i)] += 1
    for i in t:
        if arr[ord(i)] == 0:
            return False
        arr[ord(i)] -= 1
    return True


def allAnagramStrings(s,p):
    p_len = len(p)
    is_ana_str = False
    arr= []
    for i,v in enumerate(s):
        if v in p:
            is_ana_str = isAnagram(s[i:i+p_len],p)

            if is_ana_str:
                arr.append(i)
    return arr
print(allAnagramStrings("cbaebabacd","abc"))
