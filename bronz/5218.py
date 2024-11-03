import sys

T = int(input())
apn = 1
Ap = [chr(i) for i in range(ord('A'), ord('Z')+1)]
AP_dict = {}

for k in Ap:
    AP_dict[k] = apn
    apn += 1

Ip_Alpa = [sys.stdin.readline().split() for _ in range(T)]

for i in Ip_Alpa:
    a = 0
    Init_list = []
    Distance = []
    while a < len(i[0]):
        Init_list.append(i[0][a]+i[1][a])
        a += 1
    for j in Init_list:
        if int(AP_dict[j[0]]) <= int(AP_dict[j[1]]):
            Distance.append(str(int(AP_dict[j[1]])-int(AP_dict[j[0]])))
        else:
            Distance.append(str(int(AP_dict[j[1]])+26-int(AP_dict[j[0]])))
    print(f"Distances: {' '.join(Distance)} ")
            