nums = []
with open("Day08.txt", 'r') as INPUT:
    data = INPUT.read().split("\n")
    for i in data:
        a = i.split(" | ")
        nums.append((list(map(set, a[0].split(" "))), list(map(set, a[1].split(" ")))))

def get_1():
    s = 0
    for i, j in nums:
        for k in j:
            if len(k) in (2, 3, 4, 7):
                s += 1
    return s

print("part 1:", get_1())

def get_len(n, l):
    for i in n:
        if len(i) == l:
            return i
def get_2():
    total = 0
    for i, j in nums:
        codes = [set() for i in range(10)]
        codes[1] = get_len(i, 2)
        codes[7] = get_len(i, 3)
        codes[4] = get_len(i, 4)
        codes[8] = set("abcdefg")
        for k in i:
            if len(k) == 6:
                if len(k - codes[1]) == 4:
                    if len(k - codes[4]) == 2:
                        codes[9] = k
                    else:
                        codes[0] = k
                else:
                    codes[6] = k
        a = codes[7] - codes[1]
        c = codes[0] - codes[6]
        d = codes[6] - codes[0]
        b = codes[4] - codes[1] - d
        e = codes[8] - codes[9]
        g = codes[9] - codes[4] - a
        codes[2] = set.union(a, c, d, e, g)
        codes[3] = codes[8] - b - e
        codes[5] = codes[8] - c - e
        s = 0
        for digit in j:
            for num in range(10):
                if codes[num] == set(digit):
                    s = s * 10 + num
        total += s
    return total





print("part 2:", get_2())