import sys

N = int(input())
Con = []

for i in range(N):
    Con.append(int(sys.stdin.readline()))
        
Sum_Con = sum(Con)-(len(Con)-1)

print(Sum_Con)