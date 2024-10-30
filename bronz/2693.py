import sys

T = int(input())
Nums = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]

for i in Nums:
    i.sort(reverse=True)
    print(i[2])