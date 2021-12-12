connections = {}
with open("Day12.txt", 'r') as INPUT:
    data = INPUT.read().split("\n")
    for i in data:
        caves = i.split("-")
        if caves[1] != "start":
            if caves[0] in connections:
                connections[caves[0]].append(caves[1])
            else:
                connections[caves[0]] = [caves[1]]
        if caves[0] != "start":
            if caves[1] in connections:
                connections[caves[1]].append(caves[0])
            else:
                connections[caves[1]] = [caves[0]]

def get_paths():
    paths = []
    check = [["start"]]
    while True:
        new_check = []
        if len(check) == 0:
            break
        for i in check:
            if i[-1] not in connections:
                continue
            if i[-1] == "end":
                paths.append(i)
                continue
            n = set(connections[i[-1]]) - set(j for j in i if j.islower())
            for j in n:
                new_check.append(i + [j])
        check = new_check
    return paths

print("part 1:", len(get_paths()))

def get_paths2():
    paths = []
    check = [["start"]]
    while len(check):
        new_check = []
        for i in check:
            if i[-1] not in connections:
                continue
            if i[-1] == "end":
                paths.append(i)
                continue
            a = [s for s in i if s.islower()]
            dupe = len(a) > len(set(a))
            for j in connections[i[-1]]:
                if j.islower() and j in i:
                    if not dupe:
                        new_check.append(i + [j])
                else:
                    new_check.append(i + [j])
        check = new_check
    return paths

print("part 2:", len(get_paths2()))
