from pprint import pformat
def uniqueEmailAddress(emails):
    d = dict()
    counter = 0
    for email in emails:
        local_name,domain_name = email.split("@")
        local,_ = local_name.split("+")
        f_name = "".join(local.split("."))
        print(f_name)
        if f_name in d:
            if domain_name not in d.get(f_name):
                d[f_name].append(domain_name)
                counter += 1

        else:
            d[f_name] = [domain_name]
            counter += 1
    # print("Dict is: \n {}".format(pformat(d)))
    # print("Total emails sent: {}".format(counter))

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# print(emails)
print(uniqueEmailAddress(emails))


# Solution 2 with SET
# def numUniqueEmails(self, emails):
#     """
#     :type emails: List[str]
#     :rtype: int
#     """
#     ans = set()
#     for x in emails:
#         local, domain = x.split("@")
#         words = "".join((local.split("+")[0]).split("."))
#         ans.add(words + "@" + domain)
#     return len(ans)

# Solution 3 with REGEX and SET
# import re
# def numUniqueEmails(emails):
#   """
#   :type emails: List[str]
#   :rtype: int
#   """
#   result = []
#   for each in emails:
#       # res = re.match('(.*?)\++.*@(.*)',each)
#       res = re.match('(^.+)\+.*@(.+)',each)
#       print(res)
#       print(res.group(0))
#       print(res.group(1))
#       print(res.group(2))
#       import pdb
#       pdb.set_trace()
#       result.append(res.group(1).replace('.','')+'@'+res.group(2))
#   result = set(result)
#   print(result)
#   print(len(result))
#
# emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# numUniqueEmails(emails)
