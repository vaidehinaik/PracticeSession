def partitionLabel(S):
    start = 0
    end = 0
    d = dict()
    result = list()
    for i, v in enumerate(S):
        d[v] = i
    # print(d)
    for i,v in enumerate(S):
        end = max(end, d[v])
        # print(end)
        if i == end:
            result.append(i - start + 1)
            # print(result)
            start = end + 1
    return result
print(partitionLabel("ababcbacadefegdehijhklij"))

