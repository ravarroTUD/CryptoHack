def ext_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = ext_gcd(b % a, a)
        return gcd, y - (b // a) * x, x
    
# Prime numbers given from the challenge
p = 26513
q = 32321

# Find integers for u & v 
gcd, u, v = ext_gcd(p, q)

# Take the lowest number from either u or v
flag = min(u, v)

print(flag)

