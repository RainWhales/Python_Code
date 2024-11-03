import sys

T = int(input())

for i in range(T):
    Zero = 0
    N, M = map(int, input().split())
    for j in range(N,M+1):
        a = str(j)
        Zero += a.count('0')
    print(Zero)