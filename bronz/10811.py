import sys

N,M = map(int, input().split())
NL = [x for x in range(1, N+1)]

for i in range(M):
    L, R = map(int, sys.stdin.readline().split())
    NL[L-1:R] = NL[L-1:R][::-1]
    
    
print(' '.join(map(str, NL)))   