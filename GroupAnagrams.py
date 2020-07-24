def groupAnagrams(arr):
    str_dict = dict()
    for word in arr:
        sorted_str = "".join(sorted(word))
        if sorted_str in str_dict:
            str_dict[sorted_str].append(word)
        else:
            str_dict[sorted_str] = [word]
    return list(str_dict.values())
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))




