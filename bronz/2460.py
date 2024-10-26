import sys

Input_Nums = [list(map(int, sys.stdin.readline().split())) for x in range(10)]
R = 0
R_List = []

for i in Input_Nums:
    R = R - i[0] + i[1]
    R_List.append(int(R))


print(max(R_List))