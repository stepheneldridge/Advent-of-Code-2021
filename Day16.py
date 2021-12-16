bits = []
def pad_bin(a):
    while len(a) < 4:
        a  = "0" + a
    return a

with open("Day16.txt", 'r') as INPUT:
    data = INPUT.read()
    for i in data:
        bits += pad_bin(bin(int(i, 16))[2:])

total = 0
def get_next(string):
    global total
    v = int(string[0:3], 2) 
    t = int(string[3:6], 2)
    total += v
    if t == 4:
        value = 0
        index = 6
        while True:
            value <<= 4
            value += int(string[index + 1: index + 5], 2)
            if string[index] == "0":
                break
            index += 5
        return {"ver": v, "type": t, "value": value, "end": index + 5}
    else:
        i = int(string[6], 2)
        end = 0
        if i == 0:
            l = int(string[7:22], 2)
            rest = string[22:22 + l]
            start = 0
            children = []
            while start < l:
                child = get_next(rest[start:])
                start += child["end"]
                children.append(child)
            end = 22 + l
        else:
            l = int(string[7:18], 2)
            children = []
            start = 18
            for k in range(l):
                child = get_next(string[start:])
                start += child["end"]
                children.append(child)
            end = start
        return {"ver": v, "type": t, "children": children, "end": end}

tree = get_next("".join(bits))
print("part 1:", total)

def evaluate(p):
    if p["type"] == 0:
        return sum(evaluate(i) for i in p["children"])
    elif p["type"] == 1:
        s = 1
        for i in p["children"]:
            s *= evaluate(i)
        return s
    elif p["type"] == 2:
        return min(evaluate(i) for i in p["children"])
    elif p["type"] == 3:
        return max(evaluate(i) for i in p["children"])
    elif p["type"] == 4:
        return p["value"]
    else:
        a = evaluate(p["children"][0])
        b = evaluate(p["children"][1])
        if p["type"] == 5:
            return a > b
        elif p["type"] == 6:
            return a < b
        elif p["type"] == 7:
            return a == b

print("part 2:", evaluate(tree))