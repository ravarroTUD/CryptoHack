p = 29 

for ints in range(1, p):
    if pow(ints, 2) % 29 == 14:
        print(pow(ints, 2), ints, -ints)
    if pow(ints,2 ) % 29 == 6:
        print(pow(ints, 2), ints, -ints)
    if pow(ints, 2) % 29 == 11:
        print(pow(ints, 2), ints, -ints)
    
# The smallest value is the answer