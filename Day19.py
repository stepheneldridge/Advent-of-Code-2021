class Scanner:
    def __init__(self, id, points):
        self.id = id
        self.points = [self.get_rotations(i) for i in points]
        self.sets = {id: {i[0] for i in self.points}}
        self.offsets = {id: (0, 0, 0)}

    def get_rotations(self, p):
        x, y, z = p
        return [
            (x, y, z),
            (x, -z, y),
            (x, -y, -z),
            (x, z, -y),
            (-x, y, -z),
            (-x, z, y),
            (-x, -y, z),
            (-x, -z, -y),
            (y, -x, z),
            (y, -z, -x),
            (y, x, -z),
            (y, z, x),
            (-y, x, z),
            (-y, -z, x),
            (-y, -x, -z),
            (-y, z, -x),
            (z, y, -x),
            (z, x, y),
            (z, -y, x),
            (z, -x, -y),
            (-z, y, x),
            (-z, -x, y),
            (-z, -y, -x),
            (-z, x, -y)
        ]

    def sub(self, a, r1, b, r2):
        return (a[r1][0] - b[r2][0], a[r1][1] - b[r2][1], a[r1][2] - b[r2][2])

    def add(self, a, r1, b, r2):
        return (a[r1][0] + b[r2][0], a[r1][1] + b[r2][1], a[r1][2] + b[r2][2])

    def combine(self, n):
        for i in n:
            self.points.append(self.get_rotations(i))

    def rotation_offset_set(self, s, r, offset):
        return {self.add(i, r, [offset], 0) for i in s.points}

    def own_set(self):
        return {i[0] for i in self.points}

    def find_overlaps(self, s):
        for r in range(24):
            for i in self.points[:-11]:
                for j in s.points[:-11]:
                    offset = self.sub(i, 0, j, r)
                    a = self.rotation_offset_set(s, r, offset)
                    for k in self.sets:
                        b = self.sets[k]
                        if len(a & b) >= 12:
                            self.combine(a - b)
                            self.sets[s.id] = a
                            self.offsets[s.id] = offset
                            return True
        return None

scanners = []
with open("Day19.txt", 'r') as INPUT:
    data = INPUT.read().split("\n\n")
    index = 0
    for i in data:
        s = i.split("\n")[1:]
        points = []
        for j in s:
            points.append(list(map(int, j.split(","))))
        scanners.append(Scanner(index, points))
        index += 1

main = scanners[0]
scanners = scanners[1:]
while len(scanners) > 0:
    pops = []
    for i in range(len(scanners)):
        if main.find_overlaps(scanners[i]):
            pops.append(i)
    pops.reverse()
    for i in pops:
        scanners.pop(i)
print("part 1:", len(main.own_set()))
d = 0
for i in main.offsets:
    for j in main.offsets:
        a = main.offsets[i]
        b = main.offsets[j]
        d = max(abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]), d)
print("part 2:", d)