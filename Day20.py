key = []
image = dict()
with open("Day20.txt", 'r') as INPUT:
    data = INPUT.read().replace(".", "0").replace("#", "1").split("\n\n")
    key = list(map(int, list(data[0])))
    rest = data[1].split("\n")
    for i in range(len(rest)):
        a = list(map(int, list(rest[i])))
        for j in range(len(a)):
            image[(i, j)] = a[j]

default = 0
edges = []
def get(p, image):
    global edges
    if p in image:
        return image[p]
    edges.append(p)
    return default

def swap_default():
    global default
    if default == 0:
        default = key[0]
    elif default == 1:
        default = key[0b111111111]
kernel = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

def get_k(kernel, p, image):
    v = 0
    for i in kernel:
        v <<= 1
        v += get((i[1] + p[0], i[0] + p[1]), image)
    return v

def print_img(image):
    row = None
    for i, j in sorted(image.keys()):
        if i != row:
            print()
        row = i
        print("#" if image[(i, j)] else ".", end="", sep="")
    print()

def get_count(image):
    return sum(image[i] for i in image)

for index in range(50):
    edges = []
    new_image = dict()
    for i in image:
        n = get_k(kernel, i, image)
        new_image[i] = key[n]
    c_edges = edges.copy()
    for i in c_edges:
        n = get_k(kernel, i, image)
        new_image[i] = key[n]
    swap_default()
    image = new_image
    if index == 1:
        print("part 1:", get_count(image))
print("part 2:", get_count(image))
