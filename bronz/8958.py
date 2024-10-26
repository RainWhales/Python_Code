import sys

Number = int(input())

OX_list = []
OX_total = []
count = 0
Total = 0

for i in range(Number):
    OX_list.append(sys.stdin.readline().rstrip())
    
for j in OX_list:
    for k in j:
        if k == 'O':
            count += 1
            Total += count
        elif k == 'X':
            count = 0
    print(Total)
    count = 0
    Total = 0
    
