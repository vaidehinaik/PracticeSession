def defangingAnIpAddress(address):
    address = address.split(".")
    defang = "[.]".join(address)
    return defang
print(defangingAnIpAddress("1.1.1.1"))



