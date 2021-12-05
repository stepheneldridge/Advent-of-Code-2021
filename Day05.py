nums = []
with open("Day05.txt", 'r') as INPUT:
    data = INPUT.read().split("\n")
    for i in data:
        a = i.split(" -> ")
        t = a[0].split(",")
        f = a[1].split(",")
        nums.append({
            "a": (int(t[0]), int(t[1])),
            "b": (int(f[0]), int(f[1]))
        })

def get_intersections(diag=False):
    grid = dict()
    for i in nums:
        dx = i["b"][0] - i["a"][0]
        dy = i["b"][1] - i["a"][1]
        if dx != 0 and dy != 0:
            if not diag:
                continue
        steps = abs(dx) if dx != 0 else abs(dy)
        for s in range(steps + 1):
            p = (i["a"][0] + s * dx // steps, i["a"][1] + s * dy // steps)
            if p in grid:
                grid[p] += 1
            else:
                grid[p] = 1
    return sum(1 for p in grid if grid[p] > 1)

print("part 1:", get_intersections())
print("part 2:", get_intersections(diag=True))