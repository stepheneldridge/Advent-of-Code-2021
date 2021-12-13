dots = {}
folds = []
with open("Day13.txt", 'r') as INPUT:
    data = INPUT.read().split("\n")
    for i in data:
        if "," in i:
            x = i.split(",")
            dots[(int(x[0]), int(x[1]))] = "#"
        elif "fold" in i:
            f = i.split(" ")[2].split("=")
            folds.append((f[0], int(f[1])))

def fold(t, v):
    keys = list(dots.keys())
    if t == "x":
        for i in keys:
            if dots[i] != "#":
                continue
            if i[0] > v:
                dots[i] = "."
                dots[(2 * v - i[0], i[1])] = "#"
    elif t == "y":
        for i in keys:
            if dots[i] != "#":
                continue
            if i[1] > v:
                dots[i] = "."
                dots[(i[0], 2 * v - i[1])] = "#"
t, v = folds[0]
fold(t, v)
folds = folds[1:]
print("part 1:", sum(1 for i in dots if dots[i] == "#"))
for t, v in folds:
    fold(t, v)
bbox = [0, 0, 0, 0]
for i in dots:
    if dots[i] == "#":
        bbox[2] = max(i[0], bbox[2])
        bbox[3] = max(i[1], bbox[3])
print("part 2:")
for j in range(bbox[1], bbox[3] + 1):
    for i in range(bbox[0], bbox[2] + 1):
        p = (i, j)
        if p in dots:
            print(dots[p], end="")
        else:
            print(" ", end="")
    print()