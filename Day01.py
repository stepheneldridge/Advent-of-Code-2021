nums = []
with open("Day01.txt", 'r') as INPUT:
    for i in INPUT:
        try:
            x = int(i)
            nums.append(x)
        except:
            pass

def get_sum(arr, window):
    last = -1
    count = -1
    for i in range(0, len(arr) - window + 1):
        s = sum(arr[i:i + window])
        if s > last:
            count += 1
        last = s
    return count

print("part 1:", get_sum(nums, 1))
print("part 2:", get_sum(nums, 3))