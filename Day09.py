nums = dict()
with open("Day09.txt", 'r') as INPUT:
    data = INPUT.read().split("\n")
    for i in range(len(data)):
        for j in range(len(data[i])):
            nums[(i, j)] = int(data[i][j])

def get_p(n, x, y):
    if (x, y) in n:
        return n[(x, y)]
    return 10

def get_ps(n, x, y):
    return (
        get_p(n, x + 1, y),
        get_p(n, x - 1, y),
        get_p(n, x, y + 1),
        get_p(n, x, y - 1)
    )

def get_locations(x, y):
    return {(x + 1, y), (x - 1, y), (x, y + 1), (x,  y - 1)}

def flood(n, p):
    seen = set()
    look = {p}
    while True:
        new_look = set()
        if len(look) == 0:
            break
        for i in look:
            if i in seen:
                continue
            if get_p(n, i[0], i[1]) >= 9:
                continue
            seen.add(i)
            new_look |= get_locations(i[0], i[1])
        look = new_look
    return len(seen)

s = 0
sizes = []
for i, j in nums:
    p = get_p(nums, i, j)
    if p < min(get_ps(nums, i, j)):
        s += p + 1
        sizes.append(flood(nums, (i, j)))
sizes.sort()
print("part 1:", s)
print("part 2:", sizes[-3] * sizes[-2] * sizes[-1])