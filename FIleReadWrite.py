# f = open("/Users/vaidehinaik/Downloads/myfile.txt","r")
# print(f.read())
#
#
# f = open("/Users/vaidehinaik/Downloads/myfile.txt","r")
# print(f.read(2))
#
#
# f = open("/Users/vaidehinaik/Downloads/myfile.txt","r")
# print(f.readline())
# print(f.readline())
# print(f.readline())
#
#
#
# f = open("/Users/vaidehinaik/Downloads/myfile.txt","a")
# f.write("My name after marraige should be Vaidehi Naik Kshirsagar")
# f.close()
#
# f = open("/Users/vaidehinaik/Downloads/myfile.txt","r")
# print(f.read())
#
#
# f = open("/Users/vaidehinaik/Downloads/myfile.txt","w")
# f.write("My address is 1744 Birch Lake Ct, San Jose")
# f.close()
#
# f = open("/Users/vaidehinaik/Downloads/myfile.txt","r")
# print(f.read())
#
#
# f = open("/Users/vaidehinaik/Downloads/myfile.txt","a")
# f.write("My name is Vaidehi Naik")
# f.close()
#
# f = open('/Users/vaidehinaik/Downloads/myfile.txt',"r")
# print(f.read())
#
#
# f = open("/Users/vaidehinaik/Downloads/something.txt","w")
#
# import os
# os.remove("/Users/vaidehinaik/Downloads/something.txt")

#
# import os
# if os.path.exists("/Users/vaidehinaik/Downloads/myfile1.txt"):
#     os.remove("/Users/vaidehinaik/Downloads/myfile1.txt")
# else:
#     print("file does not exist")
#
# import os
# if os.path.exists("/Users/vaidehinaik/Downloads/myfile1.txt"):
#     os.remove("/Users/vaidehinaik/Downloads/myfile1.txt")
# else:
#     print("file does not exist")
#
#
# import os
# os.rmdir("/Users/vaidehinaik/Downloads/xyz")

import re

ip_adr = list()
file_path = "/Users/vaidehinaik/Downloads/myfile.txt"
with open(file_path,'r') as d:
    data = d.readlines()
    # print(data)
    for i in data:
        print(i)
        m = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', i)
        print(m)
        print("****************************\n")

x = "my cell no is 408-332-2835 or +1 (408) 332-2835"
m = re.findall(r'\d{3}-\d{3}-\d{4}|\+\d{1,3}\s\(\d{3}\)\s\d{3}-\d{4}',x)
print(m)
m1 = re.match(r'^.+(\d{3}-\d{3}-\d{4}).+(\+.+\d{4})$',x)
print(m1.group(1))
print(m1.group(2))

