nums = []
with open("Day02.txt", 'r') as INPUT:
    for i in INPUT:
        a = i.split(" ")
        d = a[0]
        try:
            x = int(a[1])
            nums.append((d, x))
        except:
            pass


def get_prod_1():
    depth = 0
    hor = 0
    for d, i in nums:
        if d == "forward":
            hor += i
        elif d == "up":
            depth -= i
        elif d == "down":
            depth += i
    return hor * depth

print("part 1:", get_prod_1())

def get_prod_2():
    depth = 0
    hor = 0
    aim = 0
    for d, i in nums:
        if d == "forward":
            hor += i
            depth += aim * i
        elif d == "up":
            aim -= i
        elif d == "down":
            aim += i
    return hor * depth
print("part 2:", get_prod_2())