import sys

N, K = map(int, input().split())

Coins = [int(sys.stdin.readline()) for _ in range(N)]
Coins.sort(reverse=True)
Coin_N = 0

for i in Coins:
    if i <= K:
        Coin_N += K // i
        K %= i
        if K == 0:
            print(Coin_N)
            exit()