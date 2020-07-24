from pprint import pformat
def numUniqueEmails(self, emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    d = dict()
    counter = 0
    for email in emails:
        local_name,domain_name = email.split("@")
        local = local_name.split("+")[0]
        f_name = "".join(local.split("."))
        # print(f_name)
        if f_name in d:
            if domain_name not in d.get(f_name):
                d[f_name].append(domain_name)
                counter += 1

        else:
            d[f_name] = [domain_name]
            counter += 1
    return counter
print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
))
