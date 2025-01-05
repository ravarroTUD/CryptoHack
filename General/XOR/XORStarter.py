# given = "label"

# print("crypto{", end="")

# for i in given:
#     print(chr(ord(i)^13), end="")

# print("}")

import struct
x=['l','a','b','e','l']
for i in x:
    
    y = ord(i)^13
    z = chr(y)
    print(z)