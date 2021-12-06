nums = []
with open("Day06.txt", 'r') as INPUT:
    data = INPUT.read().split(",")
    nums = list(map(int, data))


def get_1():
    fish = nums.copy()
    for i in range(80):
        new = 0
        for f in range(len(fish)):
            fish[f] -= 1
            if fish[f] < 0:
                new += 1
                fish[f] = 6
        for j in range(new):
            fish.append(8)
    return len(fish)

print("part 1:", get_1())

def get_2():
    r = []
    for i in range(9):
        r.append(nums.count(i))
    for i in range(256):
        n = r[0]
        r = r[1:] + [n]
        r[6] += n
    return sum(r)

print("part 2:", get_2())