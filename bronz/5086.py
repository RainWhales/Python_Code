import sys

Num = []

while True:
    Num.append(list(map(int, sys.stdin.readline().split())))
    
    if Num[-1] == [0, 0]:
        del Num[-1]
        break

for i in Num:
    if i[0] % i[1] == 0:
        print('multiple')
    elif i[1] % i[0] == 0:
        print('factor')
    else:
        print('neither')