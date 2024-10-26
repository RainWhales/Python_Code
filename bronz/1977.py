import sys

M = int(input())
N = int(input())
O = []
i = 1

while True:
    j = i**2
    if j in range(M,N+1):
        O.append(j)
    if j > N:
        break
    i += 1
    
if O != []:
    print(f'{sum(O)}')
    print(f'{min(O)}')

else:
    print('-1')