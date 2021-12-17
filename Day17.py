import re
t = []
with open("Day17.txt", 'r') as INPUT:
    data = INPUT.read()
    nums = list(map(int, re.findall(r"-?\d+", data)))
    t = [nums[0], nums[2], nums[1], nums[3]]

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

class Probe:
    def __init__(self, x, y, xv, yv, target):
        self.pos = {"x": x, "y": y}
        self.vel = {"x": xv, "y": yv}
        self.target = target
        self.my = y

    def step(self):
        self.pos["x"] += self.vel["x"]
        self.pos["y"] += self.vel["y"]
        self.vel["x"] -= sign(self.vel["x"])
        self.vel["y"] -= 1
        self.my = max(self.pos["y"], self.my)

    def in_target(self):
        if self.pos["x"] in range(self.target[0], self.target[2] + 1) and \
           self.pos["y"] in range(self.target[1], self.target[3] + 1):
           return True
        return False

    def past_target(self):
        return self.pos["y"] < self.target[1] or self.pos["x"] > self.target[2]

hits = []
for i in range(t[2] + 1):
    for j in range(t[1] - 1, 1 - t[1]):
        p = Probe(0, 0, i, j, t)
        while not p.past_target():
            p.step()
            if p.in_target():
                hits.append(p.my)
                break
print("part 1:", max(hits))
print("part 2:", len(hits))