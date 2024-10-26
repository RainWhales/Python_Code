import sys

N, X = map(int, input().split())

A = list(map(int, sys.stdin.readline().split()))

S = []

for i in A:
    if i < X:
        S.append(i)

print(*S)