import sys

T = int(input())
N = [int(sys.stdin.readline()) for _ in range(T)]
N.sort()
for i in N:
    print(i)