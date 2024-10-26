import sys


Test = int(input())
Win = []

for i in range(Test):
    Y = 0
    K = 0
    Win = []
    for j in range(9):
        Win.append(list(map(int, sys.stdin.readline().split())))
        Y += Win[j][0]
        K += Win[j][1]
        
    if Y > K:
        print('Yonsei')
    elif K > Y:
        print('Korea')
    else:
        print('Draw')
