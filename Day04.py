import re
nums = []
boards = []
with open("Day04.txt", 'r') as INPUT:
    data = INPUT.read().split("\n\n")
    nums = list(map(int, data[0].split(",")))
    for i in data[1:]:
        rows = re.split("\s+", i.strip())
        boards.append({"labels": list(map(int, rows)), "marked": set()})

def mark(bs, num):
    for i in bs:
        for j in range(len(i["labels"])):
            if i["labels"][j] == num:
                i["marked"].add(j)
    return bs

def check(board):
    m = board["marked"]
    matches = [
        {0, 1, 2, 3, 4},
        {5, 6, 7, 8, 9},
        {10, 11, 12, 13, 14},
        {15, 16, 17, 18, 19},
        {20, 21, 22, 23, 24},
        {0, 5, 10, 15, 20},
        {1, 6, 11, 16, 21}, 
        {2, 7, 12, 17, 22},
        {3, 8, 13, 18, 23},
        {4, 9, 14, 19, 24}
    ]
    for i in matches:
        if i.issubset(m):
            s = sum(board["labels"])
            for j in m:
                s -= board["labels"][j]
            return s
    return False


def get_prod_1():
    for i in nums:
        mark(boards, i)
        for j in boards:
            s = check(j)
            if s:
                return s * i

print("part 1:", get_prod_1())

def get_prod_2():
    matched = set()
    last = 0
    for i in nums:
        mark(boards, i)
        for a in range(len(boards)):
            s = check(boards[a])
            if s and a not in matched:
                matched.add(a)
                last = s * i
    return last

print("part 2:", get_prod_2())