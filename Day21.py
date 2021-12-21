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

outcomes = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
wins = [0, 0]

def find_winner(turn, p1, p2, s1, s2, m):
    global wins
    for i in outcomes:
        t = (((p1 + i) - 1) % 10) + 1
        pc = t
        sc = s1 + t
        if sc >= 21:
            wins[turn] += outcomes[i] * m
            continue
        find_winner(0 if turn else 1, p2, pc, s2, sc, m * outcomes[i])

find_winner(0, player1, player2, 0, 0, 1)
print("part 2:", max(wins))