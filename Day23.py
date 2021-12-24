import math
cost = {
    "A": 1, "B": 10, "C": 100, "D": 1000
}

def can_insert(pod, col):
    for i in col:
        if i not in (pod, "X", "_"):
            return False
    return True

best_so_far = math.inf
def dfs(h, a, b, c, d, total):
    key = (h, a, b, c, d)
    doors = (2, 4, 6, 8)
    for i in range(len(h)):
        if i in doors and h[i] != "_":
            return math.inf
    if a[0] == "X" and b[0] == "X" and c[0] == "X" and d[0] == "X":
        global best_so_far
        if total < best_so_far:
            print(h, a, b, c, d, total)
            best_so_far = total
        return total
    best = math.inf
    for p in range(len(h)):
        if p in doors:
            continue
        if h[p] == "A":
            blocked = False
            if p < 2:
                for s in range(p + 1, 2):
                    if h[s] != "_":
                        blocked = True
                        break
            else:
                for s in range(3, p):
                    if h[s] != "_":
                        blocked = True
                        break
            if blocked:
                continue
            index = a.rfind("_")
            if can_insert("A", a):
                if index >= 0:
                    na = a[:index] + "X" + a[index + 1:]
                    best = min(dfs(h[:p] + "_" + h[p + 1:], na, b, c, d, total + (abs(p - 2) + 1 + index) * cost[h[p]]), best)
        elif h[p] == "B":
            blocked = False
            if p < 4:
                for s in range(p + 1, 4):
                    if h[s] != "_":
                        blocked = True
                        break
            else:
                for s in range(5, p):
                    if h[s] != "_":
                        blocked = True
                        break
            if blocked:
                continue
            index = b.rfind("_")
            if can_insert("B", b):
                if index >= 0:
                    nb = b[:index] + "X" + b[index + 1:]
                    best = min(dfs(h[:p] + "_" + h[p + 1:], a, nb, c, d, total + (abs(p - 4) + 1 + index) * cost[h[p]]), best)
        elif h[p] == "C":
            blocked = False
            if p < 6:
                for s in range(p + 1, 6):
                    if h[s] != "_":
                        blocked = True
                        break
            else:
                for s in range(7, p):
                    if h[s] != "_":
                        blocked = True
                        break
            if blocked:
                continue
            index = c.rfind("_")
            if can_insert("C", c):
                if index >= 0:
                    nc = c[:index] + "X" + c[index + 1:]
                    best = min(dfs(h[:p] + "_" + h[p + 1:], a, b, nc, d, total + (abs(p - 6) + 1 + index) * cost[h[p]]), best)
        elif h[p] == "D":
            blocked = False
            if p < 8:
                for s in range(p + 1, 8):
                    if h[s] != "_":
                        blocked = True
                        break
            else:
                for s in range(9, p):
                    if h[s] != "_":
                        blocked = True
                        break
            if blocked:
                continue
            index = d.rfind("_")
            if can_insert("D", d):
                if index >= 0:
                    nd = d[:index] + "X" + d[index + 1:]
                    best = min(dfs(h[:p] + "_" + h[p + 1:], a, b, c, nd, total + (abs(p - 8) + 1 + index) * cost[h[p]]), best)
    for i in range(len(a)):
        if a[i] == "X":
            break
        if a[i] == "_":
            continue
        na = a[:i] + "_" + a[i + 1:]
        for p in range(1, -1, -1):
            if h[p] == "_":
                nh = h[:p] + a[i] + h[p + 1:]
                best = min(dfs(nh, na, b, c, d, total + (abs(p - 2) + 1 + i) * cost[a[i]]), best)
            elif h[p] != "X":
                break
        for p in range(3, len(h)):
            if h[p] == "_":
                nh = h[:p] + a[i] + h[p + 1:]
                best = min(dfs(nh, na, b, c, d, total + (abs(p - 2) + 1 + i) * cost[a[i]]), best)
            elif h[p] != "X":
                break
        break
    for i in range(len(b)):
        if b[i] == "X":
            break
        if b[i] == "_":
            continue
        nb = b[:i] + "_" + b[i + 1:]
        for p in range(3, -1, -1):
            if h[p] == "_":
                nh = h[:p] + b[i] + h[p + 1:]
                best = min(dfs(nh, a, nb, c, d, total + (abs(p - 4) + 1 + i) * cost[b[i]]), best)
            elif h[p] != "X":
                break
        for p in range(5, len(h)):
            if h[p] == "_":
                nh = h[:p] + b[i] + h[p + 1:]
                best = min(dfs(nh, a, nb, c, d, total + (abs(p - 4) + 1 + i) * cost[b[i]]), best)
            elif h[p] != "X":
                break
        break
    for i in range(len(c)):
        if c[i] == "X":
            break
        if c[i] == "_":
            continue
        nc = c[:i] + "_" + c[i + 1:]
        for p in range(5, -1, -1):
            if h[p] == "_":
                nh = h[:p] + c[i] + h[p + 1:]
                best = min(dfs(nh, a, b, nc, d, total + (abs(p - 6) + 1 + i) * cost[c[i]]), best)
            elif h[p] != "X":
                break
        for p in range(7, len(h)):
            if h[p] == "_":
                nh = h[:p] + c[i] + h[p + 1:]
                best = min(dfs(nh, a, b, nc, d, total + (abs(p - 6) + 1 + i) * cost[c[i]]), best)
            elif h[p] != "X":
                break
        break
    for i in range(len(d)):
        if d[i] == "X":
            break
        if d[i] == "_":
            continue
        nd = d[:i] + "_" + d[i + 1:]
        for p in range(7, -1, -1):
            if h[p] == "_":
                nh = h[:p] + d[i] + h[p + 1:]
                best = min(dfs(nh, a, b, c, nd, total + (abs(p - 8) + 1 + i) * cost[d[i]]), best)
            elif h[p] != "X":
                break
        for p in range(9, len(h)):
            if h[p] == "_":
                nh = h[:p] + d[i] + h[p + 1:]
                best = min(dfs(nh, a, b, c, nd, total + (abs(p - 8) + 1 + i) * cost[d[i]]), best)
            elif h[p] != "X":
                break
        break
    return best

print("part 1:", dfs("___________", "AB", "CD", "CA", "DB", 0))
best_so_far = math.inf
print("part 2:", dfs("___________", "ADDB", "CCBD", "CBAA", "DACB", 0))