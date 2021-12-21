player = []
with open("Day21.txt", 'r') as INPUT:
    data = INPUT.read().split("\n")
    for i in data:
        player.append(int(i.split(": ")[1]))
player1 = player[0]
player2 = player[1]
rolls = 0
turn = 0
die = 0
score = [0, 0]
while max(score) < 1000:
    rolls += 3
    s = 3 * die + 6
    if s > 297:
        if s > 300:
            s -= 100
        s -= 100
    t = (((player[turn] + s) - 1) % 10) + 1
    score[turn] += t
    player[turn] = t
    turn = 0 if turn else 1
    die = (die + 3) % 100
print("part 1:", min(score) * rolls)

outcomes = {2: 1, 3: 3, 4: 6, 5: 7, 6: 6, 7: 3, 8: 1}
cache = dict()

def find_winner(p1, p2, s1, s2):
    global cache
    if s2 >= 21:
        return [0, 1]
    key = (p1, p2, s1, s2)
    if key in cache:
        return cache[key]
    wins = [0, 0]
    for i in outcomes:
        pc = ((p1 + i) % 10) + 1
        sc = s1 + pc
        r = find_winner(p2, pc, s2, sc)
        wins[1] += r[0] * outcomes[i]
        wins[0] += r[1] * outcomes[i]
    cache[key] = wins
    return wins
print("part 2:", max(find_winner(player1, player2, 0, 0)))