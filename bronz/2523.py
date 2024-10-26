import sys

T = int(input())

for i in range(1, T+1):
    print('*'*i)

for j in range(T-1, 0, -1):
    print('*'*j)