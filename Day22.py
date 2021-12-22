import re
reboot = []
on = set()
with open("Day22.txt", 'r') as INPUT:
    data = INPUT.read().split("\n")
    for f in data:
        a = f.split(" ")
        state = 1 if a[0] == "on" else -1
        d = list(map(int, list(re.findall(r"-?\d+", a[1]))))
        x = (d[0], d[1])
        y = (d[2], d[3])
        z = (d[4], d[5])
        reboot.append((state, x, y, z))
        for i in range(-50, 51):
            if i not in range(d[0], d[1] + 1):
                continue
            for j in range(-50, 51):
                if j not in range(d[2], d[3] + 1):
                    continue
                for k in range(-50, 51):
                    if k not in range(d[4], d[5] + 1):
                        continue
                    if state > 0:
                        on.add((i, j, k))
                    else:
                        on.discard((i, j, k))
print("part 1:", len(on))

def overlap(a, b):
    return (a[0] <= b[0] and b[0] <= a[1]) or (b[0] <= a[0] and a[0] <= b[1])

def intersect(a, b):
    return overlap(a[1], b[1]) and overlap(a[2], b[2]) and overlap(a[3], b[3])

def get_overlap_cube(a, b):
    x = (max(a[1][0], b[1][0]), min(a[1][1], b[1][1]))
    y = (max(a[2][0], b[2][0]), min(a[2][1], b[2][1]))
    z = (max(a[3][0], b[3][0]), min(a[3][1], b[3][1]))
    return (-a[0], x, y, z)

def get_volume(a):
    return a[0] * (a[1][1] - a[1][0] + 1) * (a[2][1] - a[2][0] + 1) * (a[3][1] - a[3][0] + 1)

cubes = [reboot[0]]
for i in reboot[1:]:
    collisions = []
    for j in cubes:
        if intersect(i, j):
            collisions.append(get_overlap_cube(j, i))
    if i[0] > 0:
        cubes.append(i)
    cubes.extend(collisions)

print("part 2:", sum(get_volume(i) for i in cubes))