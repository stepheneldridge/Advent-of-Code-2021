import math
import heapq
stuff = dict()
with open("Day15.txt", 'r') as INPUT:
    data = INPUT.read().split("\n")
    for i in range(len(data)):
        for j in range(len(data[i])):
            stuff[(i, j)] = int(data[i][j])

start = (0, 0)
goal = (len(data) - 1, len(data[0]) - 1)

def get_neighbors(p):
    return {
        (p[0] + 1, p[1]), 
        (p[0] - 1, p[1]),
        (p[0], p[1] + 1), 
        (p[0], p[1] - 1)
    }

def get_score(m, p):
    if p in m:
        return m[p]
    else:
        return math.inf

def dijkstra(start, goal, arr):
    to_see = [(0, start)]
    score = dict()
    score[start] = 0
    while len(to_see) != 0:
        current = heapq.heappop(to_see)
        if current[1] == goal:
            return current[0]
        for i in get_neighbors(current[1]):
            s = get_score(score, current[1]) + get_score(arr, i)
            if s < get_score(score, i):
                score[i] = s
                if i not in to_see:
                    heapq.heappush(to_see, (score[i], i))

print("part 1:", dijkstra(start, goal, stuff))

new_stuff = dict()
for x in range(5):
    for y in range(5):
        for p in stuff:
            s = ((stuff[p] + x + y - 1) % 9) + 1
            new_stuff[(p[0] + x * len(data), p[1] + y * len(data[0]))] = s
goal = (5 * len(data) - 1, 5 * len(data[0]) - 1)
print("part 2:", dijkstra(start, goal, new_stuff))
