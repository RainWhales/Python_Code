import sys

DotNum = int(input())
vector = []
Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
AXIS = 0

for i in range(DotNum):
    vector.append(list(map(int, sys.stdin.readline().split())))
    
for j in vector:
    if j[0] > 0 and j[1] > 0:
        Q1 += 1
    elif j[0] > 0 and j[1] < 0:
        Q4 += 1
    elif j[0] < 0 and j[1] > 0:
        Q2 += 1
    elif j[0] < 0 and j[1] < 0:
        Q3 += 1
    elif j[0] == 0 or j[1] == 0:
        AXIS += 1
        
print(f'Q1: {Q1}\nQ2: {Q2}\nQ3: {Q3}\nQ4: {Q4}\nAXIS: {AXIS}')