
print("F(x) = x^4 + x + 1")

seed = 0b1010
state = seed

print("{:04b}".format(state))

while True:

    newbit = (state ^ (state >> 3)) & 1
    state = (state >> 1) | (newbit << 3)
    print("{:04b}".format(state))
    if state == seed:
        break

print("\n ")
print("F(x) = x^4 + x^2 + 1 ")
seed = 0b0110
state = seed
print("{:04b}".format(state))
while True:

    newbit = (state ^ (state >> 2)) & 1
    state = (state >> 1) | (newbit << 3)
    print("{:04b}".format(state))
    if state == seed:
        break

print("\n ")
print("F(x) = x^4 + x^3 + x^2 + x + 1")
seed = 0b0110
state = seed
print("{:04b}".format(seed))
while True:
    newbit = (state ^ (state >> 1)
              ^ (state >> 2) ^ (state >> 3)) & 1
    state = (state >> 1) | (newbit << 3)
    print("{:04b}".format(state))
    if state == seed:
        break
