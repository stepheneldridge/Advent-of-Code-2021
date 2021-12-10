blocks = []
with open("Day10.txt", 'r') as INPUT:
    data = INPUT.read().split("\n")
    for i in data:
        blocks.append(list(i))

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

fix_scores = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

def find_corrupt(n):
    pops = ")]}>"
    stack = []
    for i in n:
        if i not in pops:
            stack.append(i)
        else:
            if len(stack) == 0:
                return 0
            else:
                pair = stack.pop()
                if pair == "(" and i != ")":
                    return scores[i]
                if pair == "[" and i != "]":
                    return scores[i]
                if pair == "{" and i != "}":
                    return scores[i]
                if pair == "<" and i != ">":
                    return scores[i]
    return 0

def fix_incomplete(n):
    pops = ")]}>"
    stack = []
    for i in n:
        if i not in pops:
            stack.append(i)
        else:
            stack.pop()
    stack.reverse()
    score = 0
    for i in stack:
        score = score * 5 + fix_scores[i]
    return score

def filter_corrupt():
    f_blocks = []
    s = 0
    for i in range(len(blocks)):
        score = find_corrupt(blocks[i])
        if score == 0:
            f_blocks.append(blocks[i])
        s += score
    return f_blocks, s

blocks, s = filter_corrupt()
fixed = []
for i in blocks:
    fixed.append(fix_incomplete(i))
fixed.sort()
print("part 1:", s)
print("part 2:", fixed[len(fixed) // 2])