import sys

T = int(input())

SL = [sys.stdin.readline().rstrip() for _ in range(T)]

for i in SL:
    if i[0].islower():
        j = i[0].upper()+i[1:]
        print(j)
    else:
        print(i)