INPUT = open("Day01.txt", 'r')
nums = []
for i in INPUT:
    try:
        x = int(i)
        nums.append(x)
    except:
        pass

def get():
    a = -1
    last = -1
    for i in nums:
        if i > last:
            a += 1
        last = i
    return a
print("part 1:", get())

def getter():
    last = -1
    a = -1
    for i in range(0, len(nums) - 2):
        s = nums[i] + nums[i + 1] + nums[i + 2]
        if s > last:
            a += 1
        last = s
    return a

print("part 2:", getter())