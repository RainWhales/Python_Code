import sys
S = 0
l = [list(map(int, sys.stdin.readline().split())) for x in range(4)]

for i in l:
    A = S
    S -= i[0]
    S += i[1]
    if S > A:
        F = S

print(F)