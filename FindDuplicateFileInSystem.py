from collections import defaultdict

def findDuplicate(paths):
    if not paths:
        return list()
    txt_to_file_map = defaultdict(list)
    for path in paths:
        directory, f_str = path.split(" ", 1)
        file_and_text_arr = f_str.split(" ")
        for file_data in file_and_text_arr:
            file, text = file_data.split("(")
            file_path = "{}/{}".format(directory, file)
            txt_to_file_map[text].append(file_path)
    # import pprint
    # pprint.pprint(txt_to_file_map)
    # pprint.pprint(file_to_dir_map)
    result = list()
    for text, files in txt_to_file_map.items():
        # print("text {} and files {}".format(text, files))
        temp = [file for file in files]
        if len(temp) >= 2:
            result.append(temp)
    return result
print(findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
