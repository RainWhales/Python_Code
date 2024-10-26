import sys

N = []
S = 1

for i in range(9):
    N.append(int(sys.stdin.readline()))
    
print(max(N))

for j in N:
    if j != max(N):
        S += 1
    else:
        print(S)