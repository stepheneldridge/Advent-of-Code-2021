import math
poly = ""
react = dict()
with open("Day14.txt", 'r') as INPUT:
    data = INPUT.read().split("\n")
    for i in range(len(data)):
        if i == 0:
            poly = data[i]
        elif i >= 2:
            f = data[i].split(" -> ")
            react[f[0]] = f[1]

for k in range(10):
    new_poly = ""
    for i in range(len(poly) - 1):
        key = poly[i] + poly[i + 1]
        new_poly += poly[i]
        if key in react:
            new_poly += react[key]
    poly = new_poly + poly[-1]
e = set(poly)
low = len(poly)
high = 0
for i in e:
    c = poly.count(i)
    low = min(c, low)
    high = max(c, high)
print("part 1:", high - low)

pairs = dict()
for i in range(len(poly) - 1):
        key = poly[i] + poly[i + 1]
        if key in pairs:
            pairs[key] += 1
        else:
            pairs[key] = 1
for i in range(30):
    new_pairs = dict()
    for key in pairs:
        v = react[key]
        k1 = key[0] + v
        k2 = v + key[1]
        c = pairs[key]
        if k1 in new_pairs:
            new_pairs[k1] += c
        else:
            new_pairs[k1] = c
        if k2 in new_pairs:
            new_pairs[k2] += c
        else:
            new_pairs[k2] = c
    pairs = new_pairs
elements = dict()
for key in pairs:
    k1 = key[0]
    k2 = key[1]
    if k1 in elements:
        elements[k1] += pairs[key]
    else:
        elements[k1] = pairs[key]
    if k2 in elements:
        elements[k2] += pairs[key]
    else:
        elements[k2] = pairs[key]
low = math.inf
low_e = ""
high = 0
high_e = ""
for j in elements:
    c = elements[j]
    if c > high:
        high = c
        high_e = j
    if c < low:
        low = c
        low_e = j
high //= 2
low //= 2
high += [poly[0], poly[-1]].count(high_e)
low += [poly[0], poly[-1]].count(low_e)
print("part 2:", high - low)