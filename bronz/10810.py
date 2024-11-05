import sys

N, M = map(int, input().split())
Buket = [0 for _ in range(1,N+1)]

for i in range(M):
    A,B,C = map(int, sys.stdin.readline().split())
    for i in range(A-1, B):
        Buket[i] = C


print(' '.join(map(str, Buket)))
