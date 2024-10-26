import sys

def gcf(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    return (a * b) / gcf(a ,b)
    

Case = int(input())
CaseList = []

for j in range(Case):
    CaseList.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(CaseList)):
    print(f'{int(lcm(CaseList[i][0], CaseList[i][1]))}')
