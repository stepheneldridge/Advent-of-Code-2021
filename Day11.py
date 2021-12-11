cells = {}
with open("Day11.txt", 'r') as INPUT:
    data = INPUT.read().split("\n")
    for i in range(len(data)):
        for j in range(len(data[i])):
            cells[(i, j)] = int(data[i][j])

def blink_adjacent(n, p):
    adj = {
        (p[0] + 1, p[1]),
        (p[0] - 1, p[1]),
        (p[0], p[1] + 1),
        (p[0], p[1] - 1),
        (p[0] + 1, p[1] + 1),
        (p[0] - 1, p[1] + 1),
        (p[0] - 1, p[1] - 1),
        (p[0] + 1, p[1] - 1)
    }
    adj = {i for i in adj if i in n}
    for i in adj:
        n[i] += 1
    return {i for i in adj if n[i] > 9}

def generation():
    blinks = set()
    for i in cells:
        cells[i] += 1
        if cells[i] > 9:
            blinks.add(i)
    blinked = set()
    while True:
        if len(blinks) == 0:
            break
        to_blink = set()
        for i in blinks:
            to_blink |= blink_adjacent(cells, i)
            blinked.add(i)
        blinks = to_blink - blinked
    for i in blinked:
        cells[i] = 0
    return len(blinked)

i = 0
total = 0
while True:
    i += 1
    s = generation()
    total += s
    if i == 100:
        print("part 1:", total)
    if s == len(cells):
        print("part 2:", i)
        break