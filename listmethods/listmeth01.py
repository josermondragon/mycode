#!/usr/bin/env python3

proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

#this will add d,n and s
proto.extend("dns")
print(proto)

#new list to try .pop
mylist=[ "jose", "martin", "mariajose", "matthew", "daniel", "oscar"]
print(mylist)
mylist.pop(5)
print(mylist)
