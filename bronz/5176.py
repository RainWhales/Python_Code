import sys

T = int(input())

for i in range(T):
    P, M = map(int, input().split())
    K = [list(map(int, sys.stdin.readline().strip())) for _ in range(P)]
    Cnt = []
    check = []
    for j in K:
        if j in check:
            continue
        if K.count(j) >= 2:
            Cnt.append(K.count(j)-1)
            check.append(j)

    print(sum(Cnt))
        