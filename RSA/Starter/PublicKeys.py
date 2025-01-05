# Given values
message = 12
e = 65537
p = 17
q = 23

N = p * q

print(pow(message, e, N))