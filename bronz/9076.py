import sys

T = int(input())
Scores = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]

for i in Scores:
    i.sort()
    if i[3]-i[1] >= 4:
        print('KIN')
    else:
        i.remove(max(i))
        i.remove(min(i))
        print(f'{sum(i)}')