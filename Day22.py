import re
reboot = []
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

def get_collisions(n, c):
    collisions = []
    for i in n:
        if intersect(c, i):
            collisions.append(get_overlap_cube(i, c))
    return collisions

cubes = [reboot[0]]
for i in reboot[1:]:
    collisions = get_collisions(cubes, i)
    if i[0] > 0:
        cubes.append(i)
    cubes.extend(collisions)

cube = (1, (-50, 50), (-50, 50), (-50, 50))
print("part 1:", sum(-get_volume(i) for i in get_collisions(cubes, cube)))
print("part 2:", sum(get_volume(i) for i in cubes))