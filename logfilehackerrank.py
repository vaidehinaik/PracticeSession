old_file = "myfile.txt"
file = open(old_file,'r')
# print file.read()
lines = file.read().splitlines()
# for index,line in enumerate(lines):
#     print("LINE #{}: {}".format(index,line))
hostname_to_count_map = dict()
for line in lines:
    l = line.split(" ")
    if l[0] in hostname_to_count_map:
        hostname_to_count_map[l[0]] += 1
    else:
        hostname_to_count_map[l[0]] = 1
from pprint import pformat
print("My dict is: \n {}".format(pformat(hostname_to_count_map)))

new_file = "records_{}".format(old_file)
for host, count in hostname_to_count_map.items():
    file = open(new_file,"a")
    file.write("{} {}\n".format(host,count))


