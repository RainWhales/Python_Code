import sys
n = int(input())

for i in range(n):
    player_N = int(input())
    players = {}
    for j in range(player_N):
        cost, name = sys.stdin.readline().split()
        players[name] = int(cost)
    print(max(players, key = players.get))