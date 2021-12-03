nums = []
bits = 0
with open("Day03.txt", 'r') as INPUT:
    for i in INPUT:
        bits = max(bits, len(i.strip()))
        nums.append(int(i, 2))

def get_com(l, i):
    zeroes = 0
    for j in l:
        zeroes += not j & 1 << i
    return zeroes <= len(l) >> 1

def get_prod_1():
    gamma = 0
    for i in range(bits - 1, -1, -1):
        gamma  = (gamma << 1) + get_com(nums, i)
    return gamma * (gamma ^ ((1 << bits) - 1))

print("part 1:", get_prod_1())

def get_prod_2():
    o2 = nums.copy()
    for i in range(bits - 1, -1, -1):
        m = get_com(o2, i)
        o2 = list(filter(lambda v: (v >> i) & 1 == m, o2))
    co2 = nums.copy()
    for i in range(bits - 1, -1, -1):
        m = not get_com(co2, i)
        co2 = list(filter(lambda v: (v >> i) & 1 == m, co2))
        if len(co2) <= 1:
            break
    return o2[0] * co2[0]

print("part 2:", get_prod_2())