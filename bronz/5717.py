import sys

MF = []

while True:
    MF.append(list(map(int, sys.stdin.readline().split())))
    if MF[-1] == [0, 0]:
        del MF[-1]
        break
    
for i in MF:
    print(i[0]+i[1])