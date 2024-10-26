import sys

T  = int(input())

for i in range(T):
    S = int(input())
    O = int(input())
    qp = 0
    for j in range(O):
        q, p = map(int, sys.stdin.readline().split())
        qp += q*p
    print(S+qp)
        