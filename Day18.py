nums = []
with open("Day18.txt", 'r') as INPUT:
    data = INPUT.read().replace(",", "").split("\n")
    for i in data:
        a = list(i)
        for j in range(len(a)):
            try:
                a[j] = int(a[j])
            except:
                pass
        nums.append(a)

def find(n, i, d):
    j = i + d
    while j in range(len(n)):
        if type(n[j]) is int:
            return j
        j += d
    return None

def explode(n, index):
    right_i = find(n, index, 1)
    left_i = find(n, index - 2, - 1)
    x = n[index - 2]
    y = n[index - 1]
    if left_i is not None:
        n[left_i] += x
    if right_i is not None:
        n[right_i] += y
    return n[0:index - 3] + [0] + n[index + 1:]

def reduce(n):
    depth = 0
    index = 0
    for i in n:
        if i == "[":
            depth += 1
        elif i == "]":
            if depth > 4:
                return explode(n, index), True
            depth -= 1
        index += 1
    depth = 0
    index = 0
    for i in n:
        if i == "[":
            depth += 1
        elif i == "]":
            depth -= 1
        if type(i) is int and i >= 10:
            a = i // 2
            b = i - a
            n = n[0:index] + ["[", a, b, "]"] + n[index + 1:]
            if depth >= 4:
                return explode(n, index + 3), True
            return n, True
        index += 1
    return n, False

def add(a, b):
    s = ["["] + a + b + ["]"]
    go = True
    while go:
        s, go = reduce(s)
    return s

s = nums[0]
for i in nums[1:]:
    s = add(s, i)

def mag(s):
    stack = []
    for i in s:
        if type(i) is int:
            stack.append(i)
        if i == "]":
            right = stack.pop()
            left = stack.pop()
            stack.append(left * 3 + right * 2)
    return stack[0]
print("part 1:", mag(s))

m = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if i == j:
            continue
        m = max(mag(add(nums[i], nums[j])), m)
print("part 2:", m)