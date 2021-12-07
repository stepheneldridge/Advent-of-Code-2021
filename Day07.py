import math
nums = []
with open("Day07.txt", 'r') as INPUT:
    data = INPUT.read().split(",")
    nums = list(map(int, data))

def diff(n, m):
    d = 0
    for i in n:
        d += abs(i - m)
    return d

def sumn(n):
    return (n * (n + 1)) // 2

def diff2(n, m):
    d = 0
    for i in n:
        d += sumn(abs(i - m))
    return d

def get_1():
    a = min(nums)
    b = max(nums)
    d = math.inf
    for i in range(a, b + 1):
        d = min(d, diff(nums, i))
    return d

print("part 1:", get_1())

def get_2():
    a = min(nums)
    b = max(nums)
    d = math.inf
    for i in range(a, b + 1):
        d = min(d, diff2(nums, i))
    return d

print("part 2:", get_2())