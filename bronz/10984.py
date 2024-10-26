import sys

T = int(input())
C_total = 0
G_total = 0

for i in range(T):
    N = int(input())
    for j in range(N):
        C, G = sys.stdin.readline().split()
        C = int(C)
        G = float(G) * C
        C_total += C
        G_total += G
    print(C_total)
    print(f'{(G_total/C_total):.1f}')
    C_total = 0
    G_total = 0
        
