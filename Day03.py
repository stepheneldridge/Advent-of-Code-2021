nums = []
with open("Day03.txt", 'r') as INPUT:
    for i in INPUT:
        nums.append(i)

def get_prod_1():
    gamma = 0
    epsilon = 0
    for i in range(len(nums[0]) - 1):
        ones = 0
        zeroes = 0
        for j in nums:
            if j[i] == "1":
                ones += 1
            else:
                zeroes += 1
        gamma *= 2
        epsilon *= 2
        if ones > zeroes:
            gamma += 1
        else:
            epsilon += 1
    return gamma * epsilon

print("part 1:", get_prod_1())

def get_com(s, p):
    ones = 0
    zeroes = 0
    for i in s:
        if i[p] == "1":
            ones += 1
        else:
            zeroes += 1
    return ones >= zeroes

def get_prod_2():
    o2match = nums.copy()
    co2match = nums.copy()
    for i in range(len(nums[0]) - 1):
        
        no2 = []
        m = str(int(get_com(o2match, i)))
        for j in o2match:
            if j[i] == m:
                no2.append(j)
        o2match = no2

        nco2 = []
        m = str(int(not get_com(co2match, i)))
        if len(co2match) <= 1:
            continue
        for j in co2match:
            if j[i] == m:
                nco2.append(j)
        co2match = nco2
    return int(o2match[0], 2) * int(co2match[0], 2)
print("part 2:", get_prod_2())