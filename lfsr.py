print("F(x) = x^4 + x + 1")
#seed = [0b0110, 0b1001, 0b1010, 0b0101]
seed = 0b0110
state = seed

print("{:04b}".format(state))
for i in seed:
    while True:
        print("{:04b}".format(state))
        newbit = (state ^ (state >> 3)) & 1
        state = (state >> 1) | (newbit << 3)
        print("{:04b}".format(state))
        if state == seed:
            break


print("F(x) = x^4 + x^2 + 1")
seed = 0b0110
state = seed
print("{:04b}".format(state))
for i in range(20):
    print("{:04b}".format(state))
    newbit = (state ^ (state >> 2)) & 1
    state = (state >> 1) | (newbit << 3)
    print("{:04b}".format(state))
    if state == seed:
        break

print("F(x) = x^4 + x^3 + x^2 + x + 1")
seed = 0b0110
state = seed
print("{:04b}".format(seed))
while True:
    newbit = (state ^ (state >> 1) ^ (state >> 2)
              ^ (state >> 3) ^ (state >> 4)) & 1
    state = (state >> 1) | (newbit << 3)
    print("{:04b}".format(state))
    if state == seed:
        break
